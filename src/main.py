import os
import pandas as pd
from sqlalchemy import text
from elasticsearch import helpers
import urllib3
from utils import get_engine, get_es_client

# Disable SSL warnings for Elasticsearch
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_csv_data(csv_path):
    """Load data from CSV file."""
    df = pd.read_csv(csv_path)
    print(f"📂 Loaded {len(df)} records from CSV")
    return df

def clean_and_transform(df):
    """Clean and transform the data to match our schema."""
    # Create a copy to avoid modifying original
    df = df.copy()
    
    # Rename columns to match our schema
    column_mapping = {
        'hostname': 'hostname',
        'country': 'country',
        'operating_system_name': 'os_name',
        'operating_system_provider': 'os_provider',
        'operating_system_lifecycle_status': 'lifecycle_status',
        'operating_system_installation_date': 'install_date'
    }
    
    # Select and rename only the columns we need
    df = df[list(column_mapping.keys())].rename(columns=column_mapping)
    
    # Clean data
    df['country'] = df['country'].str.upper().fillna('UNKNOWN')
    df['os_name'] = df['os_name'].fillna('Unknown')
    df['os_provider'] = df['os_provider'].fillna('Unknown')
    df['lifecycle_status'] = df['lifecycle_status'].fillna('Unknown')
    df['hostname'] = df['hostname'].fillna('Unknown')
    
    # Clean install_date - extract just the date part, leave as null if invalid
    df['install_date'] = pd.to_datetime(df['install_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    # Don't fill NaN with 'Unknown' - leave as NaN/None for dates
    
    print(f"✅ Cleaned and transformed data")
    return df

def enrich(df):
    """Add risk and system age fields."""
    df = df.copy()
    
    # Add risk level based on lifecycle status
    df['risk_level'] = df['lifecycle_status'].apply(
        lambda x: 'High' if x in ['EOL', 'EOS'] else 'Low'
    )
    
    # Calculate system age - only for valid dates
    today = pd.Timestamp.now()
    df['system_age_years'] = df['install_date'].apply(
        lambda d: (
            int((today - pd.to_datetime(d, errors='coerce')).days // 365) 
            if pd.notna(d) and pd.notna(pd.to_datetime(d, errors='coerce'))
            else 0
        )
    )
    
    print(f"✅ Enriched data with risk_level and system_age_years")
    return df

def create_table(engine):
    """Create SQLite table."""
    sql = """
    CREATE TABLE IF NOT EXISTS it_assets (
      hostname TEXT, 
      country TEXT, 
      os_name TEXT,
      os_provider TEXT, 
      lifecycle_status TEXT,
      install_date TEXT
    );
    """
    with engine.begin() as con:
        con.execute(text(sql))
    print(f"✅ Created/verified it_assets table")

def store_to_sql(df, engine):
    """Store data to SQLite."""
    # Only store base columns (not enriched fields)
    base_columns = ['hostname', 'country', 'os_name', 'os_provider', 'lifecycle_status', 'install_date']
    df[base_columns].to_sql("it_assets", engine, if_exists="replace", index=False)
    print(f"✅ Stored {len(df)} records to SQLite")

def fetch_from_sql(engine):
    """Fetch data from SQLite."""
    df = pd.read_sql("SELECT * FROM it_assets", engine)
    print(f"✅ Fetched {len(df)} records from SQLite")
    return df

def index_to_elastic(df, es, index):
    """Index data to Elasticsearch."""
    # Clean the dataframe - replace NaN with None and convert to dict
    df_clean = df.copy()
    df_clean = df_clean.where(pd.notna(df_clean), None)
    
    # Convert to records and prepare for bulk indexing
    actions = []
    for i, record in enumerate(df_clean.to_dict('records')):
        # Use a unique ID for each document (use row index to ensure uniqueness)
        doc_id = f"{record.get('hostname', 'unknown')}_{i}"
        
        actions.append({
            "_index": index,
            "_id": doc_id,
            "_source": record
        })
    
    # Bulk index with error handling
    success_count = 0
    error_count = 0
    
    for ok, result in helpers.streaming_bulk(es, actions, raise_on_error=False):
        if ok:
            success_count += 1
        else:
            error_count += 1
            # Print first few errors for debugging
            if error_count <= 3:
                print(f"  ⚠️ Error: {result}")
    
    es.indices.refresh(index=index)
    
    if error_count > 0:
        print(f"⚠️  Indexed {success_count} records to Elasticsearch ({error_count} had errors)")
    else:
        print(f"✅ Indexed {success_count} records to Elasticsearch")

def main():
    # Get engine
    engine = get_engine()
    
    # Try to get ES client, skip if not configured
    try:
        es = get_es_client()
        index = os.getenv("ES_INDEX", "itassets_demo")
        es_available = True
    except ValueError as e:
        print(f"⚠️ Elasticsearch not configured: {e}")
        print("📝 Continuing without Elasticsearch indexing...")
        es = None
        index = None
        es_available = False
    
    # Path to CSV file
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'it_asset_inventory_cleaned.csv')
    
    # Load CSV data
    df = load_csv_data(csv_path)
    
    # Clean and transform
    df = clean_and_transform(df)
    
    # Create table and store to SQL
    create_table(engine)
    store_to_sql(df, engine)
    
    # Fetch from SQL and enrich
    df = enrich(fetch_from_sql(engine))
    
    # Index to Elasticsearch only if available
    if es_available:
        index_to_elastic(df, es, index)
        print(f"\n🎉 Pipeline complete! {len(df)} assets indexed to {index}")
    else:
        print(f"\n🎉 Pipeline complete! {len(df)} assets processed (SQL only)")
    
    # Print SQL table contents
    print_sql_table(engine)

def print_sql_table(engine):
    """Print the contents of the SQL table."""
    try:
        df = pd.read_sql("SELECT * FROM it_assets", engine)
        print(f"\n📋 SQL Table Contents ({len(df)} records):")
        print("=" * 80)
        print(df.to_string(index=False))
        print("=" * 80)
    except Exception as e:
        print(f"❌ Error reading SQL table: {e}")

if __name__ == "__main__":
    main()