from .order import Order
from collections import defaultdict

class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters long.")
        self._name = value

    def orders(self):
        return [order for order in Order._all_orders if order.customer is self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        coffee_orders = [order for order in Order._all_orders if order.coffee is coffee]

        if not coffee_orders:
            return None

        customer_spending = defaultdict(float)
        for order in coffee_orders:
            customer_spending[order.customer] += order.price

        most_aficionado_customer = None
        max_spending = -1.0

        for customer, total_spent in customer_spending.items():
            if total_spent > max_spending:
                max_spending = total_spent
                most_aficionado_customer = customer

        return most_aficionado_customer
