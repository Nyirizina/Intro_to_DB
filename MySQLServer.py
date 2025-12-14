import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Establish connection to MySQL Server
        # update 'password' with your actual MySQL root password
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='' 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist (avoids failure if it does)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Print error message if connection fails or query fails
        print(f"Error: {e}")

    finally:
        # Ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()