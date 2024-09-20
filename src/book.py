import csv
import os

class Book:
    def __init__(self, title, book_id, is_loaned=False):
        self.title = title
        self.book_id = book_id
        self.is_loaned = is_loaned

    def __str__(self):
        return f"{self.title}, {self.book_id}, {self.is_loaned}"

class BookManager:
    def __init__(self, file_path='data/booklist.txt'):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        books = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    title, book_id, is_loaned = row
                    books.append(Book(title, book_id, is_loaned == 'True'))
        return books

    def save_books(self):
        with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.title, book.book_id, book.is_loaned])