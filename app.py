
from flask import Flask, render_template, request, redirect

from db_manager import (
    add_order,
    get_pending_orders,
    complete_order
)
app = Flask(__name__)

@app.route("/")
def home():
    success = request.args.get("success")
    return render_template(
        "index.html",
        success=success
    )


@app.route("/submit", methods=["POST"])
def submit():

    customer_name = request.form["customer_name"].strip()
    phone_number = request.form["phone_number"].strip()
    grocery_items = request.form["grocery_items"].strip()

    if not customer_name:
        return "Customer name is required"

    if not phone_number:
        return "Phone number is required"

    if not grocery_items:
        return "Grocery items are required"

    try:

        add_order(
            customer_name,
            phone_number,
            grocery_items
        )

        return redirect("/?success=1")

    except Exception as error:

        print("Database Error:", error)

        return "Something went wrong"


@app.route("/admin")
def admin():

    try:

        orders = get_pending_orders()

        return render_template(
            "admin.html",
            orders=orders
        )

    except Exception as error:

        print("Database Error:", error)

        return "Unable to load orders"


@app.route("/complete/<int:order_id>", methods=["POST"])
def complete(order_id):

    try:

        complete_order(order_id)

        return redirect("/admin")

    except Exception as error:

        print("Database Error:", error)

        return "Unable to complete order"


if __name__ == "__main__":
    app.run(debug=True)