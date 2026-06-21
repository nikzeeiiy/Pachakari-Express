# Pachakari Express

Pachakari Express is a simple grocery order queue management web application built using Flask and MySQL. Customers can submit grocery orders through a web form, while store administrators can view pending orders and mark them as completed through an admin dashboard.

## Features

* Customer order submission form
* Admin dashboard for viewing pending orders
* Order completion workflow
* MySQL database integration
* Parameterized SQL queries to prevent SQL injection
* Frontend and backend validation
* Exception handling for database operations
* Database logic separated using `db_manager.py`
* Git version control with incremental commits

## Tech Stack

* Python
* Flask
* MySQL
* HTML5
* CSS3
* Git

## Project Structure

```text
PachakariExpress
│
├── app.py
├── db_manager.py
├── templates
│   ├── index.html
│   └── admin.html
├── static
│   └── style.css
└── README.md
```

## Database Setup

```sql
CREATE DATABASE grocery_db;

USE grocery_db;

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    grocery_items TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Installation

1. Install Python and MySQL.
2. Create the database using the SQL script above.
3. Install dependencies:

```bash
pip install flask mysql-connector-python
```

4. Update MySQL credentials in `db_manager.py`.
5. Run the application:

```bash
python app.py
```

## Usage

Open:

```text
http://127.0.0.1:5000
```

Admin Dashboard:

```text
http://127.0.0.1:5000/admin
```

## Learning Outcomes

This project demonstrates:

* Flask routing and template rendering
* Form handling using HTTP POST requests
* CRUD operations with MySQL
* Database connection management
* Input validation
* Error handling using try-except-finally
* Separation of concerns using modular design
* Git workflow and version control

```
```
