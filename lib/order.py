class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, type(self)._get_customer_class()):
            raise TypeError("Customer must be an instance of the Customer class.")
        self._customer = customer

        if not isinstance(coffee, type(self)._get_coffee_class()):
            raise TypeError("Coffee must be an instance of the Coffee class.")
        self._coffee = coffee

        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._price = price

        Order._all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @staticmethod
    def _get_customer_class():
        from .customer import Customer
        return Customer

    @staticmethod
    def _get_coffee_class():
        from .coffee import Coffee
        return Coffee
