import pandas as pd
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Load the CSV file
df = pd.read_csv(os.path.join(script_dir, 'it_asset_inventory.csv'))

# 2. Remove duplicate rows based on the 'hostname' field
df = df.drop_duplicates(subset=['hostname'])

# 3. Trim extra spaces from all text fields
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# 4. Handle blanks and missing values: Replace empty cells with 'Unknown'
df = df.replace('', 'Unknown').fillna('Unknown')

# 5. Check and fix date format under 'operating_system_installation_date'
if 'operating_system_installation_date' in df.columns:
    df['operating_system_installation_date'] = pd.to_datetime(
        df['operating_system_installation_date'], errors='coerce', dayfirst=True
    )
    df['operating_system_installation_date'] = df['operating_system_installation_date'].fillna('Unknown')

# 6. Save the cleaned data
df.to_csv(os.path.join(script_dir, 'it_asset_inventory_cleaned.csv'), index=False)

print("✅ Data cleaning completed. File saved as 'it_asset_inventory_cleaned.csv'")
print("✅ Data cleaning completed. File saved as 'it_asset_inventory_cleaned.csv'")