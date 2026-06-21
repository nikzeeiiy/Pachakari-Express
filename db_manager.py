import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grocery_db"
    )


def add_order(customer_name, phone_number, grocery_items):

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


def get_pending_orders():

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM orders
            WHERE status='Pending'
            ORDER BY created_at ASC
        """)

        return cursor.fetchall()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def complete_order(order_id):

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE orders
            SET status='Completed'
            WHERE id=%s
            """,
            (order_id,)
        )

        connection.commit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()