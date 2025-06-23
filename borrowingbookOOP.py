class BookAlreadyBorrowed(Exception):
    def __init__(self,signal):
        super().__init__(signal)
class BookWasNotBorrowed(Exception):
    def __init__(self,signal):
        super().__init__(signal)
class BookError(Exception):
    def __init__(self,signal):
        super().__init__(signal)
class NoBookAvailabilty(Exception):
    def __init__(self,signal):
        super().__init__(signal)
class Book:
    def __init__(self,author,title):
        self.author=author
        self.title=title
        self.is_borrowed=False
    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            print(f"{self.title} is borrowed")
        else:
            raise BookAlreadyBorrowed("Book already borrowed")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print("Book is returned")
        else:
            raise BookWasNotBorrowed("Book was not borrowed")
    def __str__(self):
        status=["Available" if not self.is_borrowed else "Borrowed"]
        return f"{self.title} by {self.author}-{status}"
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title,author):
        book=Book(title,author)
        self.books.append(book)
        return f"{title} by {author} added"
    def remove_book(self,title):
        for book in self.books:
            if book.title==title and not book.is_borrowed:
                self.books.remove(book)
                print("Removed the book from the library")
            return
        raise BookError("Book is either borrowed or whatever")
    def show_books(self):
        if not self.books:
            raise NoBookAvailabilty("No book available")
    def borrow_book(self,title):
        for book in self.books:
            if book.title==title:
                book.borrow()
            return
        raise NoBookAvailabilty("Not Available")
    def return_book(self,title):
        for book in self.books:
            if book.title==title:
                book.return_book()
            return
        raise BookWasNotBorrowed("Book was not borrowed")
library = Library()
library.add_book("No no", "Ali")
library.add_book("1984", "Alii")
print("\nAvailable Books:")
library.show_books()
library.borrow_book("1983")
print("\nBooks after borrowing '1984':")
library.show_books()
library.return_book("1984")
print("\nBooks after returning '1984':")
library.show_books()
library.remove_book("No no")
print("\nBooks after removing 'No no':")
library.show_books()