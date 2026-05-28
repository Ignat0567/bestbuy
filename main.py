"""Main application module providing the interactive store interface."""
from typing import List
from products import Product
from store import Store


def display_products(store_obj: Store):
    """List all available and active products in the console."""
    print("\n                 Available Products\n")
    active_products = store_obj.get_all_products()
    for index, product in enumerate(active_products, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("-------------------------------------------------")


def process_order_items(active_products: List[Product]) -> list:
    """Prompt user for products and quantities to compile the shopping list."""
    shopping_list = []
    while True:
        print("\n              Available products:\n")
        for index, prod in enumerate(active_products, start=1):
            print(f"{index}. {prod.name} Price: {prod.price}, Qty: {prod.quantity}")

        print("\n(Leave field empty and press Enter to finish order)\n")
        prod_idx_input = input("Which product do you want to buy? (Enter number): ").strip()

        if prod_idx_input == "":
            break

        try:
            prod_idx = int(prod_idx_input) - 1
            if prod_idx < 0 or prod_idx >= len(active_products):
                print("Invalid product number. Please select from the list.")
                continue

            chosen_product = active_products[prod_idx]
            quantity_input = input(f"{chosen_product.name} to buy: ").strip()

            if quantity_input == "":
                print("Quantity cannot be empty. Product not added.")
                continue

            quantity = int(quantity_input)

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            if quantity > chosen_product.get_quantity():
                print(f"Not enough stock. Only {chosen_product.get_quantity()} available.")
                continue

            shopping_list.append((chosen_product, quantity))
            print(f"Added to cart: {chosen_product.name} x{quantity}")

        except ValueError:
            print("Please enter valid numbers.")
    return shopping_list


def handle_order(store_obj: Store):
    """Manage the shopping process, trigger ordering, and print receipt."""
    print("\n                Making an Order")
    active_products = store_obj.get_all_products()

    if not active_products:
        print("Sorry, no products available right now.")
        return

    shopping_list = process_order_items(active_products)

    if shopping_list:
        try:
            total_cost = store_obj.order(shopping_list)
            total_items = sum(item[1] for item in shopping_list)

            print("\n        Order successful!")
            print("-------------------------------------")
            for product, quantity in shopping_list:
                print(f"{product.name} x {quantity} pcs. x ${product.price}\n"
                      f"Subtotal: ${quantity * product.price}\n")
            print("-------------------------------------")

            print(f"Total amount: {total_items} items")
            print(f"Total cost: ${total_cost}")
        except ValueError as error:
            print(f"\nOrder failed: {error}")
    else:
        print("\n     Order cancelled!\n"
              "       (empty cart)")


def start(store_obj: Store):
    """Execute the main loop showing the menu options to the user."""
    while True:
        print(
            "\n       Store Menu"
            "\n       ----------"
            "\n1. List all products in store"
            "\n2. Show total amount in store"
            "\n3. Make an order"
            "\n4. Quit"
        )

        user_input = input("Please choose a number: ").strip()

        if user_input == "1":
            display_products(store_obj)
        elif user_input == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal amount of items in store: {total_quantity}")
        elif user_input == "3":
            handle_order(store_obj)
        elif user_input == "4":
            print("\n   Thank you! Goodbye!\n")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 4")


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)
