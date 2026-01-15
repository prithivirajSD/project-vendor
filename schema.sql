CREATE DATABASE IF NOT EXISTS products_db;
USE products_db;

CREATE TABLE IF NOT EXISTS products_vectors (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    vector JSON
);
