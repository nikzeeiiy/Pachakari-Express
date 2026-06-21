import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="grocery_db"
    )


@app.route("/")
def home():
    success = request.args.get("success")
    return render_template("index.html", success=success)


@app.route("/submit", methods=["POST"])
def submit():

    customer_name = request.form["customer_name"]
    phone_number = request.form["phone_number"]
    grocery_items = request.form["grocery_items"]

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO orders
        (customer_name, phone_number, grocery_items)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (customer_name, phone_number, grocery_items)
        )

        connection.commit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()

    return redirect("/?success=1")


@app.route("/admin")
def admin():

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM orders
            WHERE status = 'Pending'
            ORDER BY created_at ASC
        """)

        orders = cursor.fetchall()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()

    return render_template("admin.html", orders=orders)


@app.route("/complete/<int:order_id>", methods=["POST"])
def complete(order_id):

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE orders
            SET status = 'Completed'
            WHERE id = %s
            """,
            (order_id,)
        )

        connection.commit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()

    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)