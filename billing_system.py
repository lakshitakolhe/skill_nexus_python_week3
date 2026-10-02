class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 0.05

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        subtotal = 0

        print("\n" + "=" * 60)
        print("                 BILLING SYSTEM")
        print("=" * 60)
        print(f"{'Product':<20}{'Price':>10}{'Qty':>8}{'Total':>12}")
        print("-" * 60)

        for product in self.products:
            total = product.get_total()
            subtotal += total

            print(f"{product.name:<20}{product.price:>10.2f}"
                  f"{product.quantity:>8}{total:>12.2f}")

        tax = subtotal * self.tax_rate
        final_total = subtotal + tax

        print("-" * 60)
        print(f"{'Subtotal:':>46} {subtotal:>10.2f}")
        print(f"{'Tax (5%):':>46} {tax:>10.2f}")
        print(f"{'Final Amount:':>46} {final_total:>10.2f}")
        print("=" * 60)
        print("          Thank you for shopping!")


bill = Bill()

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = Product(name, price, quantity)
    bill.add_product(product)

bill.display_bill()