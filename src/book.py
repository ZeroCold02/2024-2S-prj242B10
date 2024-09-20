class Book:
    def __init__(self, title, book_id, is_loaned=False):
        self.title = title
        self.book_id = book_id
        self.is_loaned = is_loaned

    def __str__(self):
        return f"{self.title}, {self.book_id}, {self.is_loaned}

class BookManager:
    def __init__(self, file_path='data/booklist.txt'):
        self.file_path = file_path
        self.books = self.load_books()