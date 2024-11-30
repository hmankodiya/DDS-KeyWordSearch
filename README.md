# DDS-KeyWordSearch

### README.md

# News Search Application with Elasticsearch and Flask

This project demonstrates a full-stack application to search a news dataset using Elasticsearch, Flask (backend), and a simple HTML/JavaScript frontend.

## Features
- **Full-Text Search:** Search for news articles by `title` and `text`.
- **Elasticsearch Integration:** Data is indexed and searched using Elasticsearch.
- **Frontend Interface:** User-friendly search page with dynamic result display.

---

## Project Structure

```
/project-folder
|-- app.py                # Flask backend for API and frontend rendering
|-- index_data.py         # Script to preprocess and index data into 
|-- /templates
    |-- index.html        # HTML frontend for the application
|-- news.csv              # Dataset containing news articles (title, text, label)
```

---

## Prerequisites
1. **Python** (Version 3.8 or higher recommended)
2. **Elasticsearch** (Version 8.x recommended)
3. **Dependencies**: Flask, Elasticsearch Python Client

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone <repository_url>
cd project-folder
```

### 2. Install Python Dependencies
Install the required Python libraries:
```bash
pip install flask elasticsearch
```

### 3. Start Elasticsearch
Ensure Elasticsearch is running locally or on a cloud service. Update the connection URL and credentials in `app.py` and `index_data.py`:
```python
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "your_password"),  # Replace with your credentials
    verify_certs=False,
)
```

### 4. Index the Dataset
Prepare and index the dataset using the `index_data.py` script:
```bash
python index_data.py
```

### 5. Run the Flask Application
Start the Flask app to serve the API and frontend:
```bash
flask --app app run
```

### 6. Access the Application
Open your browser and visit:
```
http://127.0.0.1:5000/
```

---

## Usage
1. **Search News Articles:**
   - Enter a query (e.g., `Donald Trump`, `economy`) in the search bar.
   - Click **Search** to view the results.
   
2. **Results Display:**
   - Articles matching the query are displayed with their `title`, `text`, and `label`.

---

## Dataset Structure (`news.csv`)
The dataset must include the following columns:
- `title`: Title of the news article
- `text`: Full text of the news article
- `label`: Category or label associated with the article

Example:
```csv
title,text,label
"Breaking News","Some news content here","politics"
"Economic Update","More news content","economy"
```
