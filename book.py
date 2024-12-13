from add_books import add_books
from view_all_books import view_all_books
from restore_books import restore_all_books
from datetime import datetime
from update_book import update_books
from remove_books import remove_books
from lend_book import lend_book, return_book


all_books = []


while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Books")
    print("4. Remove Books")
    print("5. Lend Book")
    print("6. Return Book")

    all_books = restore_all_books(all_books)
    
    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books(all_books)
    elif menu == "2":
        view_all_books(all_books)
    elif menu == "3":
        update_books(all_books)
    elif menu == "4":
        remove_books(all_books)
    elif menu == "5":
        all_books = lend_book(all_books)
    elif menu == "6":
        all_books = return_book(all_books)
    else:
        print("Choose a valid number")