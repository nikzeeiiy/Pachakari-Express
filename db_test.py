
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="grocery_db"
)

print("Database Connected!")

connection.close()