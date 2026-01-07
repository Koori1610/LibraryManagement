class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book[ID={self.id}, Title={self.title}, Author={self.author}]"
class LibraryManager:
    def __init__(self):
        self.books = []

    # Thêm sách
    def add_book(self, book):
        self.books.append(book)
        print(f"Đã thêm sách: {book.title}")

    # Xóa sách theo ID
    def remove_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print(f"Đã xóa sách ID: {book_id}")
                return True
        return False

    # Tìm sách theo ID
    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    # Hiển thị danh sách sách
    def display_books(self):
        if not self.books:
            print("Thư viện chưa có sách nào.")
            return

        for book in self.books:
            print(book)

    # Lấy toàn bộ danh sách sách
    def get_books(self):
        return self.books
