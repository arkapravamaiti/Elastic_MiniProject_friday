# IT Asset Inventory - ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.x-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.x-lightgrey.svg)

A complete ETL (Extract, Transform, Load) pipeline for managing IT asset inventory data. This project demonstrates data processing from CSV to SQLite and Elasticsearch, with data enrichment and risk analysis capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Flow](#data-flow)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This ETL pipeline processes IT asset inventory data, storing it in both SQLite (for local data persistence) and Elasticsearch (for advanced search and analytics). The pipeline includes data cleaning, transformation, enrichment with risk metrics, and system age calculations.

## ✨ Features

- **📂 CSV Data Ingestion**: Load IT asset data from CSV files
- **🧹 Data Cleaning & Transformation**: Standardize and clean asset information
- **💾 Dual Storage**: Store data in both SQLite and Elasticsearch
- **📊 Data Enrichment**: 
  - Risk level calculation based on lifecycle status
  - System age calculation from installation date
- **🔍 Data Verification**: Built-in verification tools for Elasticsearch
- **⚠️ Error Handling**: Robust error handling and logging
- **🔒 SSL Support**: Secure connection to Elasticsearch Cloud

## 🏗️ Architecture

```
CSV File → Data Loading → Cleaning/Transformation → SQLite Storage
                                    ↓
                           Data Enrichment
                                    ↓
                         Elasticsearch Indexing
```

### Data Pipeline Stages:

1. **Extract**: Load data from `it_asset_inventory_cleaned.csv`
2. **Transform**: 
   - Clean and standardize column names
   - Handle missing values
   - Convert date formats
   - Add derived fields (risk_level, system_age_years)
3. **Load**: 
   - Store in SQLite database
   - Index to Elasticsearch cluster

## 🔧 Prerequisites

- Python 3.8 or higher
- Elasticsearch Cloud account (or local Elasticsearch instance)
- pip (Python package manager)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/arkapravamaiti/Elastic_MiniProject_friday.git
   cd Elastic_MiniProject_friday
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy the `.env.sample` file to `.env` in the `src` folder
   - Update the values with your Elasticsearch credentials
   ```bash
   cp src/.env.sample src/.env
   ```

## ⚙️ Configuration

Edit the `src/.env` file with your configuration:

```bash
# SQLite path
SQLITE_PATH=./data/itassets.db

# Elasticsearch Cloud Configuration
ES_ENDPOINT=https://your-deployment.es.region.gcp.elastic.cloud:443
ES_API_KEY=your_api_key_here
ES_INDEX=itassets_demo
```

### Configuration Parameters:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `SQLITE_PATH` | Path to SQLite database file | `./data/itassets.db` |
| `ES_ENDPOINT` | Elasticsearch cluster endpoint URL | Required |
| `ES_API_KEY` | Elasticsearch API key for authentication | Required |
| `ES_INDEX` | Index name for storing assets | `itassets_demo` |

## 🚀 Usage

### Running the ETL Pipeline

```bash
cd src
python main.py
```

### Expected Output:

```
📂 Loaded 500 records from CSV
✅ Cleaned and transformed data
✅ Created/verified it_assets table
✅ Stored 500 records to SQLite
✅ Fetched 500 records from SQLite
✅ Enriched data with risk_level and system_age_years
✅ Indexed 500 records to Elasticsearch

🎉 Pipeline complete! 500 assets indexed to itassets_demo
```

### Verifying Data in Elasticsearch

```bash
cd src
python verify_es.py
```

This will display:
- Index existence status
- Total document count
- Sample document structure
- List of all asset-related indices

## 📁 Project Structure

```
Elastic_MiniProject_friday/
├── src/
│   ├── main.py           # Main ETL pipeline script
│   ├── utils.py          # Utility functions (DB & ES clients)
│   ├── verify_es.py      # Elasticsearch verification script
│   ├── .env              # Environment configuration (not in repo)
│   └── data/             # SQLite database directory
│       └── itassets.db   # SQLite database file
├── it_asset_inventory_cleaned.csv  # Source data file
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── screenshots/         # Project screenshots
    ├── Screenshot 2025-11-03 181128.png
    ├── Screenshot 2025-11-03 181145.png
    ├── Screenshot 2025-11-03 181308.png
    └── Screenshot 2025-11-03 181459.png
```

## 🔄 Data Flow

### Input Data Schema (CSV)
- `hostname`: Server hostname
- `country`: Country location
- `operating_system_name`: OS name
- `operating_system_provider`: OS provider (Windows, Linux, etc.)
- `operating_system_lifecycle_status`: Lifecycle status (Active, EOL, EOS)
- `operating_system_installation_date`: Installation date

### Output Schema (SQLite & Elasticsearch)

**Base Fields:**
- `hostname` (TEXT)
- `country` (TEXT)
- `os_name` (TEXT)
- `os_provider` (TEXT)
- `lifecycle_status` (TEXT)
- `install_date` (TEXT)

**Enriched Fields (Elasticsearch only):**
- `risk_level` (TEXT): "High" for EOL/EOS systems, "Low" otherwise
- `system_age_years` (INTEGER): Calculated from installation date

## 📸 Screenshots

The `screenshots` folder contains visual documentation of:
- Elasticsearch dashboard views
- Data visualization in Kibana
- Query results and analytics
- Pipeline execution logs

## 🛠️ Development

### Key Functions in `main.py`:

| Function | Purpose |
|----------|---------|
| `load_csv_data()` | Load data from CSV file |
| `clean_and_transform()` | Clean and standardize data |
| `enrich()` | Add risk_level and system_age_years |
| `create_table()` | Create SQLite table schema |
| `store_to_sql()` | Save data to SQLite |
| `fetch_from_sql()` | Retrieve data from SQLite |
| `index_to_elastic()` | Index data to Elasticsearch |
| `print_sql_table()` | Display SQLite table contents |

### Utility Functions in `utils.py`:

| Function | Purpose |
|----------|---------|
| `get_engine()` | Create SQLAlchemy engine for SQLite |
| `get_es_client()` | Create Elasticsearch client connection |

## 🔍 Troubleshooting

### Common Issues:

**Issue**: `ValueError: Please set ES_ENDPOINT and ES_API_KEY in .env`
- **Solution**: Ensure `.env` file exists in `src` folder with valid credentials

**Issue**: SSL Certificate Verification Failed
- **Solution**: The code includes `verify_certs=False` for demo purposes. For production, use proper SSL certificates.

**Issue**: No data in Elasticsearch
- **Solution**: Run `python verify_es.py` to check index status and connection

## 📊 Data Quality

The pipeline includes:
- ✅ Null value handling
- ✅ Date format standardization
- ✅ Text normalization (uppercase country codes)
- ✅ Duplicate prevention using unique document IDs
- ✅ Error logging for failed indexing operations

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is created for educational purposes as part of a training program.

## 👤 Author

**Arkaprava Maiti**
- GitHub: [@arkapravamaiti](https://github.com/arkapravamaiti)

## 📅 Project Timeline

- **Created**: November 3, 2025
- **Last Updated**: November 4, 2025

---

**Note**: This project demonstrates ETL pipeline concepts, data processing with Python, and integration with modern data storage solutions (SQLite & Elasticsearch).
