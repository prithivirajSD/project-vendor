import csv
import random

electronics = [
    "Apple iPhone 14", "Apple iPhone 14 Pro", "Samzung Galaxy S21",
    "Samsung Galaxy S22", "OnePlus 11", "One Plus 11",
    "Sony WH-1000XM5 Headphones", "Sony WH1000XM5"
]

fashion = [
    "Nike Running Shoes", "Nkie Running Shoes",
    "Adidas Sports T-Shirt", "Adiddas Sports T-Shirt",
    "Levi's Denim Jeans", "Levis Denim Jeans"
]

groceries = [
    "Organic Almonds 500g", "Organic Almond 500gm",
    "Aashirvaad Wheat Flour", "Ashirvad Wheat Flour",
    "Fortune Sunflower Oil 1L", "Fortune Sunflower Oil 1 Liter"
]

all_products = electronics + fashion + groceries

rows = []
for i in range(1, 501):
    product_name = random.choice(all_products)
    rows.append([i, product_name])

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["product_id", "product_name"])
    writer.writerows(rows)

print("✅ products.csv generated with 500 products")
