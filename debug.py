from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order
def run_debug_script():
    print("--- Coffee Shop Debug Script ---")

#Creates Customers
    print("\nCreating Customers:")
    customer1 = Customer("Josphine")
    customer2 = Customer("Peter")
    customer3 = Customer("Biomdo")
    print(f"Customer 1: {customer1.name}")
    print(f"Customer 2: {customer2.name}")
    print(f"Customer 3: {customer3.name}")

 # Test name property setter and it should raise error if it is invalid
    try:
        customer1.name = "ThisIsALongNameIndeed"
    except ValueError as e:
        print(f"Caught expected error for long name: {e}")
    try:
        customer1.name = 123
    except TypeError as e:
        print(f"Caught expected error for non-string name: {e}")
    customer1.name = "Josphine"
    print(f"Customer 1 new name: {customer1.name}")

 # Creates Coffees
    print("\nCreating Coffees:")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    coffee3 = Coffee("Cappuccino")
    print(f"Coffee 1: {coffee1.name}")
    print(f"Coffee 2: {coffee2.name}")
    print(f"Coffee 3: {coffee3.name}")

    try:
        coffee1.name = "New Espresso" 
    except AttributeError as e: 
        print(f"Caught expected error for immutable coffee name: {e}")


# Create Orders
    print("\nCreating Orders via Customer.create_order():")
    order1 = customer1.create_order(coffee1, 4.50)
    order2 = customer1.create_order(coffee2, 3.00)
    order3 = customer2.create_order(coffee1, 4.00)
    order4 = customer3.create_order(coffee3, 5.50)
    order5 = customer2.create_order(coffee3, 5.75)
    order6 = customer3.create_order(coffee2, 3.25)

    print(f"Order 1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")
    print(f"Order 2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")
    print(f"Order 3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")
    print(f"Order 4: {order4.customer.name} ordered {order4.coffee.name} for ${order4.price}")
    print(f"Order 5: {order5.customer.name} ordered {order5.coffee.name} for ${order5.price}")
    print(f"Order 6: {order6.customer.name} ordered {order6.coffee.name} for ${order6.price}")

    try:
        order1.price = 5.00
    except AttributeError as e:
        print(f"Caught expected error for immutable order price: {e}")

    print("\n--- Testing Object Relationships ---")

# Customer.orders()
    print(f"\nOrders for {customer1.name}:")
    for order in customer1.orders():
        print(f"  - {order.coffee.name} (${order.price})") 

    print(f"\nCoffees ordered by {customer1.name}:")
    for coffee_obj in customer1.coffees():
        print(f"  - {coffee_obj.name}")

    print(f"\nOrders for {coffee1.name}:") 
    for order in coffee1.orders():
        print(f"  - {order.customer.name} (${order.price})")

    print(f"\nCustomers who ordered {coffee1.name}:")
    for customer in coffee1.customers():
        print(f"  - {customer.name}")

    print("\n--- Testing Aggregates & Associations ---")

    print(f"\nNumber of orders for {coffee1.name}: {coffee1.num_orders()}")
    print(f"Number of orders for {coffee2.name}: {coffee2.num_orders()}")
    print(f"Number of orders for {coffee3.name}: {coffee3.num_orders()}")

    print(f"Average price for {coffee1.name}: ${coffee1.average_price():.2f}")
    print(f"Average price for {coffee2.name}: ${coffee2.average_price():.2f}")
    print(f"Average price for {coffee3.name}: ${coffee3.average_price():.2f}")

    coffee_no_orders = Coffee("Decaf")
    print(f"Average price for {coffee_no_orders.name} (no orders): ${coffee_no_orders.average_price():.2f}")

    print("\n--- Testing Bonus Method ---")
    most_aficionado_latte = Customer.most_aficionado(coffee1)
    if most_aficionado_latte:
        print(f"Most aficionado for {coffee1.name}: {most_aficionado_latte.name}")
    else:
        print(f"No aficionado for {coffee1.name} yet.")

    most_aficionado_espresso = Customer.most_aficionado(coffee2)
    if most_aficionado_espresso:
        print(f"Most aficionado for {coffee2.name}: {most_aficionado_espresso.name}")
    else:
        print(f"No aficionado for {coffee2.name} yet.")

    most_aficionado_decaf = Customer.most_aficionado(coffee_no_orders)
    if most_aficionado_decaf:
        print(f"Most aficionado for {coffee_no_orders.name}: {most_aficionado_decaf.name}")
    else:
        print(f"No aficionado for {coffee_no_orders.name} yet.")

    print("\n--- Debug Script Finished ---")

if __name__ == "__main__":
    run_debug_script()


    