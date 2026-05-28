"""Module containing the Store class for managing products."""
from typing import List, Tuple
from products import Product


class Store:
    """Manages a collection of products and processes user orders."""

    def __init__(self, products: List[Product]):
        """Initialize the store with a list of products."""
        self.products = list(products)

    def add_product(self, product: Product):
        """Add a new unique product to the store inventory."""
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product: Product):
        """Remove an existing product from the store inventory."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all items in the store stock."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        """Return a list containing only the active products in store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Process a batch purchase and return the total order cost."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
