# coffee-shop-challenge
Welcome to this simple Python project that models a coffee shop using object-oriented programming. It’s a great example of how classes, relationships, and data can work together in Python.

Think of it like:  
1. Customers walk into the shop and order coffee.  
2. We track who orders what, how much they spend, and more — all using Python classes.

## What’s Inside

This project builds a small system:

- A **Coffee** has many **Orders**.
- A **Customer** has many **Orders**.
- An **Order** connects a **Customer** to a **Coffee**and it includes how much they paid.

### Customer
->Create a customer with a name (1–15 characters).
->Get or set their name with validation.
->See all their orders.
->See all the different coffees they’ve tried.
->Place a new order with a coffee and a price.

### Coffee
->Create a coffee with a name.
->Get its name.
->See all orders placed for this coffee.
->See all customers who ordered it.
->Count how many times it’s been ordered.
->Calculate the average price customers pay for it.

### Order
->Create an order with a customer, a coffee, and a price (between 1.0–10.0).
->Get the customer and coffee linked to it.
->Get the price.
->Behind the scenes, every order is stored in a central list, so we can easily look up and connect everything.

## Getting Started

Here’s how to run the application in your machine:

### 1. Clone the Project
git clone git@github.com:<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge
### 2. Set Up Your Environment (Using Pipenv)
pipenv install
pipenv shell
This will create a virtual environment for you. No extra dependencies are needed.

### 3. Run the Example
python debug.py
This script will show the system in action: adding customers and coffees, placing orders, and printing out some fun stats.
