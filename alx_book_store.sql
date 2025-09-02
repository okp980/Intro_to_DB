DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Author;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Order;
DROP TABLE IF EXISTS Order_Details;

CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE Book(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id FOREIGN KEY REFERENCES Author(author_id),
    price DOUBLE NOT NULL,
    publication_date DATE NOT NULL
);

CREATE TABLE Author(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

CREATE TABLE Customer(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT NOT NULL
)

CREATE TABLE Order(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES Customer(customer_id),
    order_date DATE NOT NULL
)

CREATE TABLE Order_Details(
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES Order(order_id),
    book_id INT FOREIGN KEY REFERENCES Book(book_id),
    quantity DOUBLE NOT NULL
)