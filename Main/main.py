from Manager import Book
from Manager import LibraryManager

if __name__ == "__main__":
    manager = LibraryManager()

    manager.add_book(Book(1, "Clean Code", "Robert C. Martin"))
    manager.add_book(Book(2, "Python Core", "Mark Lutz"))

    manager.display_books()

    manager.remove_book_by_id(1)
    manager.display_books()
