import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv("./news.csv")

    # Preprocessing (if required)
    df.dropna(inplace=True)  # Drop rows with missing values

    # Convert to Elasticsearch-friendly JSON format
    documents = []
    for i, row in df.iterrows():
        documents.append(
            {
                "_index": "news",
                "_id": i,
                "_source": {
                    "title": row["title"],
                    "text": row["text"],
                    "label": row["label"],
                },
            }
        )

    # Connect to Elasticsearch
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "tFQQr4EXuesRrKgqYJMX"),  # change key here
        verify_certs=False,
    )

    # Index the documents
    bulk(es, documents)
    print("Data indexed successfully.")
