import json
import os

FILE = "books.json"
books = []

def load_books():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            books.extend(json.load(f))

def save_books():
    with open(FILE, "w") as f:
        json.dump(books, f, indent=4)

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def add_book():
    book_id = input("Enter book ID: ")
    if find_book(book_id):
        print("This ID already exists!")
        return
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books.append({"id": book_id, "title": title,
                  "author": author, "issued": False})
    save_books()
    print("Book added successfully!")

def view_books():
    if not books:
        print("No books in library.")
        return
    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print(book["id"], "|", book["title"], "|", book["author"], "|", status)

def search_book():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(book["id"], "|", book["title"], "|", book["author"])
            found = True
    if not found:
        print("No book found.")

def issue_book():
    book = find_book(input("Enter book ID to issue: "))
    if book is None:
        print("Book not found.")
    elif book["issued"]:
        print("Book is already issued.")
    else:
        book["issued"] = True
        save_books()
        print("Book issued!")

def return_book():
    book = find_book(input("Enter book ID to return: "))
    if book is None:
        print("Book not found.")
    elif not book["issued"]:
        print("This book was not issued.")
    else:
        book["issued"] = False
        save_books()
        print("Book returned!")

def delete_book():
    book = find_book(input("Enter book ID to delete: "))
    if book is None:
        print("Book not found.")
    else:
        books.remove(book)
        save_books()
        print("Book deleted!")

load_books()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
        