# IT Asset Inventory - Mini Project (CSV Version)

This project loads IT asset data from a CSV file, stores it in SQLite, and indexes it to Elasticsearch for visualization in Kibana.

## Project Structure

```
miniProjectTRy/
├── src/
│   ├── main.py         # Main pipeline script (CSV-based)
│   ├── utils.py        # Helper functions (DB & ES)
│   └── verify_es.py    # Verification script
├── data/               # Created automatically
│   └── itassets.db     # SQLite database
├── .env                # Configuration
├── requirements.txt    # Dependencies
└── it_asset_inventory_cleaned.csv  # Source data
```

## Features

✅ Loads data from CSV file (instead of generating fake data)
✅ Cleans and transforms data
✅ Stores in SQLite database
✅ Enriches with calculated fields (risk_level, system_age_years)
✅ Indexes to Elasticsearch
✅ Ready for Kibana visualization

## Data Fields

### From CSV (Base Fields):
- `hostname` - Server hostname
- `country` - Country location
- `os_name` - Operating system name
- `os_provider` - OS provider (Microsoft, RedHat, etc.)
- `lifecycle_status` - Status (Active, EOL, EOS, etc.)
- `install_date` - Installation date

### Enriched Fields (Calculated):
- `risk_level` - High (if EOL/EOS) or Low
- `system_age_years` - Age in years since installation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure `.env` file with your Elasticsearch credentials:
```
SQLITE_PATH=./data/itassets.db
ES_ENDPOINT=https://your-cluster.es.cloud:443
ES_API_KEY=your_api_key_here
ES_INDEX=itassets_demo
```

## Usage

### Run the pipeline:
```bash
cd src
python main.py
```

This will:
1. Load data from CSV
2. Clean and transform it
3. Store in SQLite
4. Enrich with calculated fields
5. Index to Elasticsearch

### Verify the data:
```bash
cd src
python verify_es.py
```

## Expected Output

```
📂 Loaded 330 records from CSV
✅ Cleaned and transformed data
✅ Created/verified it_assets table
✅ Stored 330 records to SQLite
✅ Fetched 330 records from SQLite
✅ Enriched data with risk_level and system_age_years
✅ Indexed 330 records to Elasticsearch

🎉 Pipeline complete! 330 assets indexed to itassets_demo
```

## Kibana Setup

1. Go to Kibana → Stack Management → Data Views
2. Create data view:
   - Name: `IT Assets`
   - Index pattern: `itassets_demo`
   - Timestamp: None
3. Go to Discover and explore your data!

## Differences from Original Mini Project

| Original | CSV Version |
|----------|-------------|
| Uses Faker to generate 500 fake records | Uses real CSV data (330 records) |
| All data is generated randomly | Data is loaded and cleaned from CSV |
| Fixed data schema | Adapts to CSV schema |

## Key Features

- **Data Cleaning**: Handles missing values, standardizes formats
- **Flexible**: Easy to swap different CSV files
- **Same Pipeline**: Rest of the flow identical to original project
- **Production Ready**: Works with real-world messy data

---
Created with reference to the mini_project
