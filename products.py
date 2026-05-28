"""Module containing the Product class for store items."""


class Product:
    """Represents a product with name, price, quantity, and active status."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize the product and validate correct input values."""
        if not name:
            raise ValueError("The name of product can't be empty")
        if price < 0:
            raise ValueError("The price can't be negative")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current stock quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set a new stock quantity. Deactivate if quantity reaches 0."""
        if quantity < 0:
            raise ValueError("Quantity can't be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product for users to buy."""
        self.active = True

    def deactivate(self):
        """Deactivate the product from the store."""
        self.active = False

    def show(self):
        """Print the formatted product representation to the console."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buy a specific quantity. Update stock and return total cost."""
        if quantity <= 0:
            raise ValueError("The quantity to be purchased must be greater than 0")
        if not self.active:
            raise ValueError("You cannot purchase an inactive product")
        if quantity > self.quantity:
            raise ValueError("We do not have enough stock to fulfil your order")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return float(quantity * self.price)
