import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

def verify_data():
    """Verify data in Elasticsearch."""
    endpoint = os.getenv("ES_ENDPOINT")
    api_key = os.getenv("ES_API_KEY")
    index = os.getenv("ES_INDEX", "itassets_demo")
    
    # Connect to Elasticsearch
    es = Elasticsearch(endpoint, api_key=api_key, verify_certs=False)
    
    # Check if index exists
    if es.indices.exists(index=index):
        print(f"✅ Index '{index}' exists!")
        
        # Get count of documents
        count = es.count(index=index)
        print(f"📊 Total documents: {count['count']}")
        
        # Get a sample document
        result = es.search(index=index, size=1)
        if result['hits']['hits']:
            print("\n📄 Sample document:")
            print(result['hits']['hits'][0]['_source'])
        
        # List all indices
        print("\n📋 All indices:")
        indices = es.cat.indices(format='json')
        for idx in indices:
            if 'itassets' in idx['index']:
                print(f"  - {idx['index']} ({idx['docs.count']} docs)")
    else:
        print(f"❌ Index '{index}' does not exist!")
        print("\n📋 Available indices:")
        indices = es.cat.indices(format='json')
        for idx in indices:
            print(f"  - {idx['index']}")

if __name__ == "__main__":
    verify_data()
