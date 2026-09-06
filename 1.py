from datetime import datetime

class Book:
    def __init__ (self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = True
    
    def getInfo(self):
        return f" {self.title} {self.author} {self.isbn}"
    
    def borrow(self):
        self.isAvailable = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def returnBook(self):
        self.isAvailable = True

class Member:
    def __init__ (self, name, memberId, borrowedBooks):
        self.name = name
        self.memberId = memberId
        if borrowedBooks == None:
            self.borrowedBooks = []
        else:
            self.borrowedBooks = borrowedBooks
        self.isAvailible = True
    
    def getInfo(self):
        return f"{self.name} {self.memberId} {self.borrowedBooks}"
    
    def borrowBook(self, book):
        if len(self.borrowedBooks) <= 2:
            self.borrowedBooks.append(book)
            borrowTrack1.addTrack(self, book)
            book.isAvailable = False
        else: print("Максимальное число книг")

    def returnBook(self, book):
        if book.isAvailable == False:
            self.borrowedBooks.remove(book)
            book.isAvailable = True
        else:
            print("Невозможно вернуть книгу")
    
    def __str__(self):
        return f"{self.name}  {self.memberId}"

class Library:
    def __init__ (self, name, books, members):
        self.name = name
        self.books = []
        self. members = []
    
    def addBook(self, book):
        self.books.append(book)

    def registerMember(self, member):
        self.members.append(member)
    
    def lendBook(self, member, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.isAvailable:
                    if len(member.borrowedBooks) <= 2:
                        member.borrowBook(book)
                        book.borrow()
                        print(f"Книга '{book.title}' выдана {member.name}")
                        return True
                    else:
                        print("У читателя максимальное число книг")
                        return False
                else:
                    print("Книга не доступна в данный момент")
                    return False
        print("Не существующий ISBN")
        return False
    
    def recieveBook(self, member, isbn):
        for book in member.borrowedBooks:
            if book.isbn == isbn:
                member.returnBook(book)
                book.returnBook()
                print(f"Книга '{book.title}' возвращена читетелем {member.name}")
                return True
        return False
    
    def displayAvailableBooks(self):
        for book in self.books:
            if book.isAvailable:
                print(book)
class borrowTrack:
    def __init__(self, members, books, dates):
        self.members = []
        self.books = []
        self.dates = []
    
    def addTrack(self, member, book):
        self.members.append(member)
        self.books.append(book)
        date = datetime.now()
        self.dates.append(date)
    
    def displayTrack(self):
        i=0
        for i in range(len(self.dates)):
            print(f"{self.members[i]} {self.books[i]} {self.dates[i]}")
            i+=1
        
    
    

borrowTrack1 = borrowTrack([], [], [])
book1 = Book("Design Patterns", "Gang of Four", "978-0201633610")
book2 = Book("Clean Code", "Robert Martin", "978-0132350884")
book3 = Book("BAba", "Robert Martin", "978-0132350123")
book4 = Book("Sas", "Gang of Four", "978-02043563610")
book5 = Book("Mam", "Robert Martin", "978-0132884")
book6 = Book("Dadada", "Robert Martin", "-0132350123")

library1 = Library("ABS", [], [])
library1.addBook(book1)
library1.addBook(book2)
library1.addBook(book3)
library1.addBook(book4)
library1.addBook(book5)
library1.addBook(book6)

print(book1.getInfo())
book1.borrow()
print(book1.isAvailable)
book1.returnBook()
print(book1.isAvailable)

member1 = Member("Jon", "0", [])
member2 = Member("Man", "123", [])

library1.registerMember(member1)
library1.registerMember(member2)

member1.borrowBook(book1)
print(member1.borrowedBooks[0])

print("\n")
library1.displayAvailableBooks()

library1.lendBook(member2, "978-0132350123")
library1.lendBook(member2, "978-02043563610")
library1.lendBook(member2, "978-0132884")
library1.lendBook(member2, "-0132350123")
library1.lendBook(member1, "-0132sdfgsdf123")

library1.recieveBook(member1, "978-0201633610")

borrowTrack1.displayTrack()
