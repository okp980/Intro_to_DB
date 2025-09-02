#!/usr/bin/env python3
"""
MySQL Table Creation Script
Creates all tables in the alx_book_store database
"""

import mysql.connector
from mysql.connector import Error

def create_tables():
    """
    Creates all tables in the alx_book_store database
    """
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Default MySQL user, change if needed
            password=""   # Add your MySQL password here if required
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_database_query)
            
            # Use the database
            cursor.execute("USE alx_book_store")
            
            # Drop existing tables if they exist (in reverse order of dependencies)
            drop_tables_queries = [
                "DROP TABLE IF EXISTS Order_Details",
                "DROP TABLE IF EXISTS Orders", 
                "DROP TABLE IF EXISTS Books",
                "DROP TABLE IF EXISTS Authors",
                "DROP TABLE IF EXISTS Customers"
            ]
            
            for query in drop_tables_queries:
                cursor.execute(query)
            
            # Create Authors table first (no dependencies)
            create_authors_table = """
            CREATE TABLE Authors (
                author_id INT AUTO_INCREMENT PRIMARY KEY,
                author_name VARCHAR(215) NOT NULL
            )
            """
            cursor.execute(create_authors_table)
            print("Table 'Authors' created successfully!")
            
            # Create Customers table (no dependencies)
            create_customers_table = """
            CREATE TABLE Customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(215) NOT NULL,
                email VARCHAR(215) NOT NULL,
                address TEXT NOT NULL
            )
            """
            cursor.execute(create_customers_table)
            print("Table 'Customers' created successfully!")
            
            # Create Books table (depends on Authors)
            create_books_table = """
            CREATE TABLE Books (
                book_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(130) NOT NULL,
                author_id INT,
                price DOUBLE NOT NULL,
                publication_date DATE NOT NULL,
                FOREIGN KEY (author_id) REFERENCES Authors(author_id)
            )
            """
            cursor.execute(create_books_table)
            print("Table 'Books' created successfully!")
            
            # Create Orders table (depends on Customers)
            create_orders_table = """
            CREATE TABLE Orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                order_date DATE NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            )
            """
            cursor.execute(create_orders_table)
            print("Table 'Orders' created successfully!")
            
            # Create Order_Details table (depends on Orders and Books)
            create_order_details_table = """
            CREATE TABLE Order_Details (
                orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT,
                book_id INT,
                quantity DOUBLE NOT NULL,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                FOREIGN KEY (book_id) REFERENCES Books(book_id)
            )
            """
            cursor.execute(create_order_details_table)
            print("Table 'Order_Details' created successfully!")
            
            print("\nAll tables created successfully in 'alx_book_store' database!")
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close database connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_tables()
