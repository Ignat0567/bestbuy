class Product:
    def __init__(self, name: str, price: float, quantity: int):
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
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity can't be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int):
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
