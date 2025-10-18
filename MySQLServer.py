#!/usr/bin/python3
"""
A simple script to create the 'alx_book_store' database in MySQL using PyMySQL.
"""

import pymysql

def create_database():
    connection = None
    try:
        # Connect to MySQL Server
        connection = pymysql.connect(
            host="localhost",
            user="root",             # change if needed
            password="@sql-Software-0745464042" # replace with your MySQL password
        )

        with connection.cursor() as cursor:
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()