# EASY TASK
class Rectangle:
    shape = "Rectangle"
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width

# Rect1 = Rectangle(10, 20)
# Rect2 = Rectangle(5, 25)
# print(Rect1.shape)
# print(Rect1.area())
# print(Rect2.area())

# MEDIUM TASK

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount: int):
        if amount < self.balance:   
            self.balance = self.balance - amount  
            print(f"Amount withdrawn! Current Balance: {self.balance}")
        else:
            print(f"You do not have this amount! Current Balance: {self.balance}")
    def deposit(self, amount: int):
        self.balance = self.balance + amount  
        print(f"Amount deposited! Current Balance: {self.balance}")
    def get_balance(self):
        print(f"Your current balance is: {self.balance}")

# Adam = BankAccount(20000)
# Adam.deposit(1000)
# Adam.withdraw(2000)
# Adam.withdraw(50000)
# Adam.get_balance()

# HARD TASK

class Book:
    def __init__(self, title: str, author: str, available_copies: int):
        self.title = title
        self.author = author
        self.available_copies = available_copies
    def __str__(self):
        return f"\"{self.title}\" by {self.author} (available_copies: {self.available_copies})"

class Library:
    def __init__(self):
        self.books = []
        self.borrowed = []
    def add_book(self, book: Book):
        self.books.append(book)
    def borrow_book(self, title: str):
        update = False
        for e in self.books:
            if e.title == title:
                if e.available_copies > 0:
                    print(f"You have borrowed the book \"{e.title}\" by {e.author}")
                    e.available_copies -= 1
                    self.borrowed.append(e)
                    update = True
                else:
                    print("There are no available copies of this book.")
                    update = True
        if update == False:
            print("We do not have this book in the Library")
    def return_book(self, title):
        update = False
        for i in self.borrowed:
            if i.title == title:
                print(f"You have returned the book \"{i.title}\" by {i.author}")
                i.available_copies += 1
                self.borrowed.remove(i)
                update = True
        if update == False:
            print("You have not borrowed this book.")
    def list_books(self):
        for i in self.books:
            print(f"{i.title}, ")

# Improvements, replace update flags with return to escape.
def borrow_book_s(self, title: str):
        for e in self.books:
            if e.title == title:
                if e.available_copies > 0:
                    print(f"You have borrowed the book \"{e.title}\" by {e.author}")
                    e.available_copies -= 1
                    self.borrowed.append(e)
                    return
                else:
                    print("There are no available copies of this book.")
                    return
        print("We do not have this book in the Library")
def return_book_s(self, title):
        for i in self.borrowed:
            if i.title == title:
                print(f"You have returned the book \"{i.title}\" by {i.author}")
                i.available_copies += 1
                self.borrowed.remove(i)
                return
        print("You have not borrowed this book.")
        
# # Create books
# book1 = Book("1984", "George Orwell", 3)
# book2 = Book("The Hobbit", "J.R.R. Tolkien", 2)

# # Create library and add books
# library = Library()
# library.add_book(book1)
# library.add_book(book2)

# # Borrow and return
# library.borrow_book("1984")
# library.borrow_book("The Hobbit")
# library.return_book("1984")

# # List all books
# library.list_books()

