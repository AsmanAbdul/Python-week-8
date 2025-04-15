class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You've borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.available = True
        print(f"'{self.title}' has been returned.")

    def display_details(self):
        availability = "Available" if self.available else "Unavailable"
        print(f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nYear: {self.year}\nStatus: {availability}")


# Subclass to explore polymorphism (e.g., "Ebook")
class Ebook(Book):
    def __init__(self, title, author, genre, year, file_size):
        super().__init__(title, author, genre, year)
        self.file_size = file_size

    def borrow_book(self):
        print(f"You've borrowed the ebook '{self.title}' by {self.author}. Enjoy reading on your device!")

    def display_details(self):
        super().display_details()
        print(f"File Size: {self.file_size} MB")

# Creating objects
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
book.display_details()
book.borrow_book()
book.return_book()

ebook = Ebook("The Martian", "Andy Weir", "Science Fiction", 2011, 2.5)
ebook.display_details()
ebook.borrow_book()
