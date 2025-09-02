#!/usr/bin/env python3
"""
MySQL Database Creation Script
Creates the alx_book_store database in MySQL server
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL server
    """
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Default MySQL user, change if needed
            password=""   # Add your MySQL password here if required
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            # Using CREATE DATABASE IF NOT EXISTS to avoid errors if database already exists
            create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_database_query)
            
            # Verify database exists by trying to use it
            cursor.execute("USE alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
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
    create_database()
