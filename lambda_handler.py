import json
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def lambda_handler(event, context):
    query = event.get("query", "")

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT product_id, product_name FROM products_vectors")
    rows = cursor.fetchall()
    conn.close()

    product_ids = [r[0] for r in rows]
    product_names = [r[1] for r in rows]

    vectorizer = TfidfVectorizer()
    product_vectors = vectorizer.fit_transform(product_names)

    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, product_vectors)[0]

    top_indices = similarities.argsort()[-5:][::-1]

    results = []
    for idx in top_indices:
        results.append({
            "product_id": product_ids[idx],
            "product_name": product_names[idx],
            "score": float(similarities[idx])
        })

    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }
