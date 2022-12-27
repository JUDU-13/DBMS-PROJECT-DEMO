# This is a simple full stack DBMS project in Python and SQL Plus for a railway ticket booking website with 8 tables

# Import the necessary modules
import cx_Oracle
from flask import Flask, render_template, request

# Connect to the database
conn = cx_Oracle.connect("user/password@host:port/sid")

# Create a cursor
cursor = conn.cursor()

# Create the tables
cursor.execute("CREATE TABLE customers (id NUMBER PRIMARY KEY, name VARCHAR2(100), address VARCHAR2(200))")
cursor.execute("CREATE TABLE orders (id NUMBER PRIMARY KEY, customer_id NUMBER, date DATE)")
cursor.execute("CREATE TABLE order_items (id NUMBER PRIMARY KEY, order_id NUMBER, product_id NUMBER, quantity NUMBER)")
cursor.execute("CREATE TABLE products (id NUMBER PRIMARY KEY, name VARCHAR2(100), price NUMBER)")
cursor.execute("CREATE TABLE suppliers (id NUMBER PRIMARY KEY, name VARCHAR2(100), address VARCHAR2(200))")
cursor.execute("CREATE TABLE product_suppliers (id NUMBER PRIMARY KEY, product_id NUMBER, supplier_id NUMBER)")
cursor.execute("CREATE TABLE employees (id NUMBER PRIMARY KEY, name VARCHAR2(100), salary NUMBER)")
cursor.execute("CREATE TABLE stations (id NUMBER PRIMARY KEY, name VARCHAR2(100), location VARCHAR2(200))")

# Save the changes
conn.commit()

# Close the connection
conn.close()

# Create the Flask app
app = Flask(__name__)

# Define the routes
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
  # Get the booking information from the form
  destination = request.form["destination"]
  num_tickets = int(request.form["num_tickets"])
  customer_name = request.form["customer_name"]
  customer_address = request.form["customer_address"]
  
  # Calculate the ticket price
  ticket_price = num_tickets * 50
  
  # Connect to the database
  conn = cx_Oracle.connect("user/password@host:port/sid")
  
  # Create a cursor
  cursor = conn.cursor()
  
  # Insert the customer into the database
  cursor.execute("INSERT INTO customers (name, address) VALUES (:1, :2)", (customer_name, customer_address))
  
  # Get the customer's ID
  cursor.execute("SELECT id FROM customers WHERE name = :1 AND address = :2", (customer_name, customer_address))
  customer_id = cursor.fetchone()[0]
  
  # Insert the order into the database
  cursor.execute("INSERT INTO orders (customer_id, date) VALUES (:
