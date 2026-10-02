class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b


calc = Calculator()

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Result:", calc.add(a, b))
    elif choice == "2":
        print("Result:", calc.subtract(a, b))
    elif choice == "3":
        print("Result:", calc.multiply(a, b))
    elif choice == "4":
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid choice!")

except ValueError:
    print("Error: Please enter valid numbers!")

except ZeroDivisionError as e:
    print("Error:", e)