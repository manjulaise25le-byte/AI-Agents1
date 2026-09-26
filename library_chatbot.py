
books = [
    {
        "name": "Python Crash Course",
        "author": "Eric Matthes",
        "category": "Python",
        "available": True
    },
    {
        "name": "Java Complete Reference",
        "author": "Herbert Schildt",
        "category": "Java",
        "available": True
    },
    {
        "name": "Clean Code",
        "author": "Robert C. Martin",
        "category": "Programming",
        "available": False
    },
    {
        "name": "Introduction to Algorithms",
        "author": "Thomas Cormen",
        "category": "Algorithms",
        "available": True
    },
    {
        "name": "Computer Networks",
        "author": "Andrew Tanenbaum",
        "category": "Networking",
        "available": True
    }
]


def print_book(book):
    status = "Available" if book["available"] else "Not Available"
    print(f"\nBook Name : {book['name']}")
    print(f"Author    : {book['author']}")
    print(f"Category  : {book['category']}")
    print(f"Status    : {status}")


def find_books(field, query):
    query = query.strip().lower()
    if not query:
        return []
    return [book for book in books if query in book[field].lower()]


def show_books(results, title="BOOKS"):
    print(f"\n========== {title} ==========")
    for book in results:
        print_book(book)
    print("\n" + "=" * (len(title) + 22))


def show_all_books():
    show_books(books, "ALL BOOKS")


def search_books(field, prompt, empty_message):
    results = find_books(field, input(prompt))
    if results:
        show_books(results, "SEARCH RESULTS")
    else:
        print(f"\n{empty_message}")


def search_book():
    search_books("name", "\nEnter book name: ", "Book not found.")


def search_author():
    search_books("author", "\nEnter author name: ", "No books found for this author.")


def search_category():
    search_books("category", "\nEnter category: ", "No books found in this category.")


def check_availability():
    results = find_books("name", input("\nEnter book name: "))
    if not results:
        print("\nBook not found.")
        return

    for book in results:
        print(f"\nBook: {book['name']}")
        if book["available"]:
            print("Status: AVAILABLE")
            print("You can borrow this book.")
        else:
            print("Status: NOT AVAILABLE")
            print("This book is currently borrowed.")


def update_availability(available):
    results = find_books("name", input("\nEnter book name: "))
    if not results:
        print("\nBook not found.")
        return

    book = results[0]
    if book["available"] == available:
        status = "available" if available else "already borrowed"
        print(f"\n'{book['name']}' is {status}.")
        return

    book["available"] = available
    action = "borrowed" if not available else "returned"
    print(f"\n'{book['name']}' has been {action} successfully.")


def main():
    print("\n======================================")
    print("       COLLEGE LIBRARY CHATBOT")
    print("======================================")

    actions = {
        "1": show_all_books,
        "2": search_book,
        "3": search_author,
        "4": search_category,
        "5": check_availability,
        "6": lambda: update_availability(False),
        "7": lambda: update_availability(True),
    }

    while True:
        print("\nWhat would you like to do?")
        print("\n1. Show All Books")
        print("2. Search Book")
        print("3. Search Author")
        print("4. Search Category")
        print("5. Check Book Availability")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()
        if choice == "8":
            print("\nThank you for using College Library Chatbot!")
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("\nInvalid choice! Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
