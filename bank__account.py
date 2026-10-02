class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Current Balance: Rs.", self.balance)


account = BankAccount()
while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")

