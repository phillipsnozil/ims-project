class Product:
    def __init__(self, product_id, name, category, price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_stock(self, product_id, quantity_sold):
        for product in self.products:
            if product.product_id == product_id:
                if product.quantity_in_stock >= quantity_sold:
                    product.quantity_in_stock -= quantity_sold
                    return True
                else:
                    return False
        return False

    def get_product_info(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None


class Transaction:
    def __init__(self, transaction_id, products, total_amount):
        self.transaction_id = transaction_id
        self.products = products
        self.total_amount = total_amount


class InventoryManagementSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.transactions = []
        self.transaction_id_counter = 1

    def add_product(self, product_id, name, category, price, quantity_in_stock):
        product = Product(product_id, name, category, price, quantity_in_stock)
        self.inventory.add_product(product)

    def process_sale(self, products_sold):
        total_amount = 0
        sold_products = {}
        for product_id, quantity in products_sold.items():
            product = self.inventory.get_product_info(product_id)
            if product and product.quantity_in_stock >= quantity:
                total_amount += product.price * quantity
                sold_products[product.name] = quantity
                if not self.inventory.update_stock(product_id, quantity):
                    return "Insufficient stock for product ID: {}".format(product_id)
            else:
                return "Invalid product ID or insufficient stock for product ID: {}".format(product_id)

        transaction = Transaction(self.transaction_id_counter, sold_products, total_amount)
        self.transactions.append(transaction)
        self.transaction_id_counter += 1
        return "Transaction successful. Total amount: ${}".format(total_amount)

    def display_sales_history(self):
        print("\nSales History:")
        for transaction in self.transactions:
            print("Transaction ID: {}".format(transaction.transaction_id))
            for product, quantity in transaction.products.items():
                print("Product: {}, Quantity: {}".format(product, quantity))
            print("Total Amount: ${}\n".format(transaction.total_amount))
def main():
    ims = InventoryManagementSystem()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Process Sale")
        print("3. Display Sales History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Quantity in Stock: "))
            ims.add_product(product_id, name, category, price, quantity)
            print("Product added successfully!")

        elif choice == "2":
            products_sold = {}
            while True:
                product_id = int(input("Enter Product ID to sell (0 to finish): "))
                if product_id == 0:
                    break
                quantity = int(input("Enter Quantity to sell: "))
                products_sold[product_id] = quantity
            result = ims.process_sale(products_sold)
            print(result)

        elif choice == "3":
            ims.display_sales_history()

        elif choice == "4":
            print("Exiting the Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

