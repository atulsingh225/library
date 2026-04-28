# Library system

# Lists to store books
available_books = []
issued_books = []

# Function to add a book
def add_book():
    book = input("Enter book name to add: ")
    available_books.append(book)
    print(f"'{book}' added to library.\n")

# Function to issue a book
def issue_book():
    book = input("Enter book name to issue: ")
    if book in available_books:
        available_books.remove(book)
        issued_books.append(book)
        print(f"'{book}' issued successfully.\n")
    else:
        print("Book not available.\n")

# Function to show all books
def show_books():
    print("\nAvailable Books:", available_books)
    print("Issued Books:", issued_books)

    # Merged list
    all_books = available_books + issued_books
    print("All Books (Merged):", all_books, "\n")

# Main menu
while True:
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Show Books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        issue_book()
    elif choice == '3':
        show_books()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.\n")
