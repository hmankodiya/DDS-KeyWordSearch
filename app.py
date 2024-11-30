from flask import Flask, request, jsonify, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Elasticsearch connection
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "tFQQr4EXuesRrKgqYJMX"),  # Replace with your credentials
    verify_certs=False,
)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    try:
        res = es.search(
            index="news",
            body={"query": {"multi_match": {"query": query, "fields": ["title", "text"]}}},
        )
        return jsonify(res["hits"]["hits"])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
