class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book in self.books:
            print("Book already exists!")
        else:
            self.books.append(book)
            print("Book added successfully!")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found!")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book is not available!")

    def return_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print("Book returned successfully!")
        else:
            print("Book is already in the library!")

    def display_books(self):
        print("\nAvailable Books:")
        if self.books:
            for book in self.books:
                print("-", book)
        else:
            print("No books available!")


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        book = input("Enter book name to remove: ")
        library.remove_book(book)

    elif choice == "3":
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")