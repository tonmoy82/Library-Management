import json
from datetime import datetime, timedelta
from save_all_books import save_all_books

LENT_BOOKS_FILE = "lent_books.json"

# Helper function to load lent books
def load_lent_books():
    try:
        with open(LENT_BOOKS_FILE, "r") as fp:
            return json.load(fp)
    except FileNotFoundError:
        return []

# Helper function to save lent books
def save_lent_books(lent_books):
    with open(LENT_BOOKS_FILE, "w") as fp:
        json.dump(lent_books, fp, indent=4)

# Function to lend a book
def lend_book(all_books):
    lent_books = load_lent_books()

    title = input("Enter the title of the book to lend: ")
    for book in all_books:
        if book["title"] == title:
            if book["quantity"] > 0:
                borrower_name = input("Enter borrower's name: ")
                phone_number = input("Enter borrower's phone number: ")
                due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

                lent_books.append({
                    "title": title,
                    "borrower_name": borrower_name,
                    "phone_number": phone_number,
                    "due_date": due_date
                })

                book["quantity"] -= 1
                save_all_books(all_books)
                save_lent_books(lent_books)

                print(f"Book '{title}' lent successfully to {borrower_name}. Due date: {due_date}")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books

    print("Book not found.")
    return all_books

# Function to return a book
def return_book(all_books):
    lent_books = load_lent_books()

    title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter borrower's name: ")

    for lent_book in lent_books:
        if lent_book["title"] == title and lent_book["borrower_name"] == borrower_name:
            lent_books.remove(lent_book)

            for book in all_books:
                if book["title"] == title:
                    book["quantity"] += 1
                    save_all_books(all_books)
                    save_lent_books(lent_books)
                    print(f"Book '{title}' returned successfully by {borrower_name}.")
                    return all_books

    print("Lending record not found.")
    return all_books
