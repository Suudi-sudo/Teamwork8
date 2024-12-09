# qeustion 1
class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def author_title(self):
        print(f"Author: {self.author.name}",f"book: {self.title}")   
author1 = Author("suudi abdi  |") 
author2 = Author("Gorge orwell  |")
author3 = Author("peter  |")

book1 = Book("harry potter and the philosopher's stone", author1)
book2 = Book("1984", author2)
book3 = Book("puple hibiscus",author3)

book1.author_title()
book2.author_title()
book3.author_title()

