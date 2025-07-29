class Book:
    def __init__(self, title, author): #constructor
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self): 
        if self.borrowed == True:
            status = "This book is currently in use!"
        else:
            status = "This book is currently available!"
        return f"'{self.title}' by {self.author} ({status})"

class Library:
    def __init__(self):
        self.books = []

    #method to add books to library
    def addBook(self, title, author): 
        book = Book(title, author) #creating new Book object; basically creating a book with the title and author and saving in the variable book
        self.books.append(book) #adding book to the list self.books by append()
        print(f"\033[34mBook added: {book}\033[0m") #displaying formatted string

    #method to show the books in library    
    def showBooks(self): 
        if len(self.books) == 0: #checking if the book is in the list is empty
            print("\033[34mNo books in the library.\033[0m")
            return
        print("\nBooks in the library:")
        for i, book in enumerate(self.books, start=1): #using enumerate function to list the books
            print(f"{i}. {book}")

    #method to borrow the books in the library
    def borrowBook(self, title):
        for book in self.books: #looking in the list
            if book.title.lower() == title.lower(): #checking if book title is the same as the title entered that user wants to borrow
                if book.borrowed == True: #if book borrowed, do this
                    print("\033[34mSorry, that book is already borrowed.\033[0m")
                else: #if book not borrowed, set the value of book.borrow to True and then do this
                    book.borrowed = True
                    print(f"\033[34mYou borrowed: {book.title}\033[0m")
                return
        print("Book not found.")

    #method to return the book
    def returnBook(self, title):
        for book in self.books: #looking in the list
            if book.title.lower() == title.lower(): #checking if book title is the same as the title entered that user wants to borrow
                if book.borrowed: #if book borrowed, set the value of book.borrowed to False then do this
                    book.borrowed = False
                    print(f"\033[34mYou returned: {book.title}\033[0m")
                else:
                    print("\033[34mThat book was not borrowed.\033[0m")
                return
        print("Book not found.")

def main():

    library = Library() #creating a new library object so we can use the methods

    #acts as an interface, but only console

    #looping through options for library
    while True:
        print("Welcome to the Campbell Library!")
        print("___________ Library Menu ___________ ")
        print("\033[31m1. Enter \"A\" to add a book!\033[0m")
        print("\033[31m2. Enter \"S\" to show the list of books!\033[0m")
        print("\033[31m3. Enter \"B\" to borrow a book!\033[0m")
        print("\033[31m4. Enter \"R\" to return a book!\033[0m")
        print("\033[31m5. Enter \"E\" to exit the application!\033[0m")
        #if-elif-else structure to control what happens
        choice = input("Choose an option: ").strip()

        if choice == "A":
            title = input("Book title: ").strip()
            author = input("Book author: ").strip()
            library.addBook(title, author)

        elif choice == "S":
            library.showBooks()

        elif choice == "B":
            title = input("Title to borrow: ").strip()
            library.borrowBook(title)

        elif choice == "R":
            title = input("Title to return: ").strip()
            library.returnBook(title)

        elif choice == "E":
            print("Thanks for visiting the Campbell library")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
