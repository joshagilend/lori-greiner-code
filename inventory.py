# Lori Greiner-inspired inventory management system
# This program helps small businesses manage their product inventory effectively.

class Product:
    def __init__(self, name, cost, price, quantity):
        self.name = name
        self.cost = cost
        self.price = price
        self.quantity = quantity

    def calculate_profit_margin(self):
        return ((self.price - self.cost) / self.price) * 100

    def update_quantity(self, amount):
        self.quantity += amount

    def display_product_info(self):
        print(f"Product: {self.name}")
        print(f"Cost: ${self.cost}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Profit Margin: {self.calculate_profit_margin():.2f}%\n")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def display_inventory(self):
        print("\nInventory:")
        for product in self.products:
            product.display_product_info()

    def search_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None

# Example usage
if __name__ == "__main__":
    # Create an inventory instance
    inventory = Inventory()

    # Add some products
    product1 = Product("Phone Case", 5.00, 15.00, 100)
    product2 = Product("Wireless Earbuds", 20.00, 50.00, 50)
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Display inventory
    inventory.display_inventory()

    # Search for a product
    search_name = "Phone Case"
    found_product = inventory.search_product(search_name)
    if found_product:
        print(f"\nFound product: {search_name}")
        found_product.display_product_info()

    # Update product quantity
    found_product.update_quantity(25)

    # Remove a product
    inventory.remove_product("Wireless Earbuds")

    # Display updated inventory
    inventory.display_inventory()
