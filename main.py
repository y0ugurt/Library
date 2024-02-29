import sqlite3

class Library:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS books
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         title TEXT, author TEXT, description TEXT, genre TEXT)''')
        self.conn.commit()

    #Создание функции для добавления книги
    def add_book(self, title, author, description, genre):
        self.c.execute("INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)",
                      (title, author, description, genre))
        self.conn.commit()

    #Создание функции для Просмотра списка книг
    def view_books(self):
        self.c.execute("SELECT title, author FROM books")
        books = self.c.fetchall()
        for book in books:
            print(book)
    
    #Создание функции для поиска книг (По Автору | По названию)
    def search_books(self, keyword):
        self.c.execute("SELECT title, author FROM books WHERE title LIKE ? OR author LIKE ?", ('%'+keyword+'%', '%'+keyword+'%'))
        books = self.c.fetchall()
        for book in books:
            print(book)
            
    #Создание функции для удаления книги
    async def delete_book(self, title):
        self.c.execute("DELETE FROM books WHERE title=?", (title,))
        self.conn.commit()

# Создание экземпляра класса Library
library = Library('library.db')

# Пример использования функций
library.add_book("Book Title", "Author Name", "Description", "Genre")
library.view_books()
library.search_books("Author")
library.delete_book("Book Title")

library.conn.close()