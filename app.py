import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/submit", methods=["POST"])
def submit():

    customer_name = request.form["customer_name"]
    phone_number = request.form["phone_number"]
    grocery_items = request.form["grocery_items"]

    connection = None
    cursor = None

    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="grocery_db"
        )

        cursor = connection.cursor()

        query = """
        INSERT INTO orders
        (
            customer_name,
            phone_number,
            grocery_items
        )
        VALUES
        (%s, %s, %s)
        """

        values = (
            customer_name,
            phone_number,
            grocery_items
        )

        cursor.execute(query, values)

        connection.commit()

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

    return "Order Saved Successfully"
@app.route("/admin")
def admin():

    connection = None
    cursor = None

    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="grocery_db"
        )

        cursor = connection.cursor()

        query = """
        SELECT *
        FROM orders
        WHERE status = 'Pending'
        ORDER BY created_at ASC
        """

        cursor.execute(query)

        orders = cursor.fetchall()

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

    return render_template(
        "admin.html",
        orders=orders
    )

if __name__ == "__main__":
    app.run(debug=True)