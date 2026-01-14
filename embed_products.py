import sqlite3
import csv
import json
from sklearn.feature_extraction.text import TfidfVectorizer

print("✅ Script started")

# Step 1: Connect to SQLite
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Step 2: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products_vectors (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    vector TEXT
)
""")
print("✅ SQLite table ready")

# Step 3: Load CSV
product_ids = []
product_names = []

with open("products.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product_ids.append(int(row["product_id"]))
        product_names.append(row["product_name"])

print(f"✅ Loaded {len(product_names)} products from CSV")

# Step 4: Generate TF-IDF vectors
vectorizer = TfidfVectorizer(ngram_range=(1,2))
vectors = vectorizer.fit_transform(product_names).toarray()
print("✅ TF-IDF vectors generated")

# Step 5: Insert into SQLite
for pid, name, vec in zip(product_ids, product_names, vectors):
    cursor.execute(
        "INSERT OR REPLACE INTO products_vectors (product_id, product_name, vector) VALUES (?, ?, ?)",
        (pid, name, json.dumps(vec.tolist()))
    )

conn.commit()
conn.close()
print("✅ All products inserted into SQLite")
print("✅ Script finished")
