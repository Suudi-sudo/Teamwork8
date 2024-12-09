class Book:  
    def __init__(self, title, author):  
        self.title = title  
        self.author = author  
        self.is_borrowed = False  
        self.borrowed_by = None   

    def lend(self, member):  
        if not self.is_borrowed:  
            self.is_borrowed = True  
            self.borrowed_by = member  
            return True  
        return False  

    def return_book(self):  
        self.is_borrowed = False  
        self.borrowed_by = None  


class Member:  
    def __init__(self, name):  
        self.name = name  
        self.borrowed_books = []  

    def borrow_book(self, book):  
        if len(self.borrowed_books) < 3 and book.lend(self):  
            self.borrowed_books.append(book)  
            return True  
        return False  

    def return_book(self, book):  
        if book in self.borrowed_books:  
            book.return_book()  
            self.borrowed_books.remove(book)  

    def borrowing_history(self):  
        return [book.title for book in self.borrowed_books]  


class Library:  
    def __init__(self):  
        self.books = []  
        self.members = []  

    def add_book(self, book):  
        self.books.append(book)  

    def add_member(self, member):  
        self.members.append(member)  

    def lend_book(self, member, book):  
        if member in self.members and book in self.books:  
            if member.borrow_book(book):  
                print(f"{member.name} borrowed '{book.title}'.")  
            else:  
                print(f"{member.name} cannot borrow '{book.title}'. Limit reached or book already borrowed.")  
        else:  
            print("Member or book not found.")  

    def return_book(self, member, book):  
        if member in self.members and book in self.books:  
            member.return_book(book)  
            print(f"{member.name} returned '{book.title}'.")  
        else:  
            print("Member or book not found.")  

    def display_available_books(self):  
        available_books = [book.title for book in self.books if not book.is_borrowed]  
        print("Available books:")  
        for title in available_books:  
            print(f"- {title}")  

    def display_borrowing_history(self, member):  
        if member in self.members:  
            history = member.borrowing_history()  
            print(f"{member.name}'s Borrowing History: {', '.join(history) if history else 'No books borrowed.'}")  
        else:  
            print("Member not found.")  

 
if __name__ == "__main__":  
    library = Library()  

     
    book1 = Book("1984", "George Orwell")  
    book2 = Book("To Kill a Mockingbird", "Harper Lee")  
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")  
    book4 = Book("Moby Dick", "Herman Melville")  

    library.add_book(book1)  
    library.add_book(book2)  
    library.add_book(book3)  
    library.add_book(book4)  

    
    member1 = Member("suudi")  
    member2 = Member("peter")  

    library.add_member(member1)  
    library.add_member(member2)  

     
    library.lend_book(member1, book1)  
    library.lend_book(member1, book2)  
    library.lend_book(member1, book3)  
    library.lend_book(member1, book4)  


    library.display_available_books()  

    
    library.display_borrowing_history(member1)  

    
    library.return_book(member1, book2)  

    
    library.display_available_books()