# 🚀 Quick Start Guide

## Get Started in 5 Minutes!

### Prerequisites
- Python 3.8+
- Git
- Elasticsearch Cloud account (or local instance)

---

## Step 1: Clone Repository

```bash
git clone https://github.com/arkapravamaiti/Elastic_MiniProject_friday.git
cd Elastic_MiniProject_friday
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Configure Environment

```bash
# Copy the environment template
cp src/.env.sample src/.env

# Edit src/.env with your credentials
# Use any text editor (notepad, vim, code, etc.)
```

**Update these values in `src/.env`:**
```bash
ES_ENDPOINT=https://your-cluster.es.region.cloud.elastic.co:443
ES_API_KEY=your_api_key_here
ES_INDEX=itassets_demo
```

## Step 4: Run the Pipeline

```bash
cd src
python main.py
```

**Expected Output:**
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

## Step 5: Verify Data

```bash
python verify_es.py
```

---

## 🎯 What This Does

1. **Loads** IT asset data from CSV
2. **Cleans** and transforms the data
3. **Stores** in SQLite database
4. **Enriches** with risk levels and system age
5. **Indexes** to Elasticsearch for analytics

---

## 📊 View Results in Kibana

1. Login to Elastic Cloud
2. Go to Kibana
3. Create Index Pattern: `itassets_demo`
4. Explore data in Discover
5. Create visualizations and dashboards

---

## 🆘 Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'pandas'`
```bash
pip install -r requirements.txt
```

**Issue:** `ValueError: Please set ES_ENDPOINT and ES_API_KEY`
```bash
# Make sure src/.env exists and has correct values
cat src/.env  # On Unix/Mac
type src\.env  # On Windows
```

**Issue:** Connection Error to Elasticsearch
- Verify ES_ENDPOINT URL is correct
- Check ES_API_KEY is valid
- Ensure network connectivity

---

## 📚 Next Steps

- Read [README.md](README.md) for detailed documentation
- Check [WORKFLOW.md](WORKFLOW.md) for Git workflow
- See [SETUP_COMPLETE.md](SETUP_COMPLETE.md) for full setup info

---

**Need Help?** Check the detailed documentation in README.md
