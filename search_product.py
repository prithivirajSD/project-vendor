import sqlite3
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("✅ Script started")

# -----------------------------
# 1. Load products from DB
# -----------------------------
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute("SELECT product_id, product_name FROM products_vectors")
rows = cursor.fetchall()
conn.close()

product_ids = [row[0] for row in rows]
product_names = [row[1] for row in rows]

print(f"✅ Loaded {len(product_names)} products")

# -----------------------------
# 2. Fit TF-IDF ONCE
# -----------------------------
vectorizer = TfidfVectorizer()
product_vectors = vectorizer.fit_transform(product_names)

# -----------------------------
# 3. User query
# -----------------------------
query = input("Enter product search text: ")
query_vector = vectorizer.transform([query])

# -----------------------------
# 4. Cosine similarity
# -----------------------------
similarities = cosine_similarity(query_vector, product_vectors)[0]

top_indices = similarities.argsort()[-5:][::-1]

print("\n🔍 Top 5 similar products:\n")

for idx in top_indices:
    print(
        f"Product ID: {product_ids[idx]} | "
        f"Name: {product_names[idx]} | "
        f"Score: {similarities[idx]:.4f}"
    )

print("\n✅ Search completed")
