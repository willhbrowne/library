'''
Created on Jan 25, 2023

@author: willbrowne
'''
from User import User

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
    
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.num_of_nodes = 0
    
    def __iter__(self):
        node = self.head_node
        while node is not None:
            yield node
            node = node.next

    def list_size(self):
        return self.num_of_nodes
    
    def insert_at_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.next_node = self.head_node
            self.head_node = new_node
            
    def insert_at_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.head_node is None:
            self.head_node = new_node
        else:
            temp_node = self.head_node
            while temp_node.next_node is not None:
                temp_node = temp_node.next_node
            temp_node.next_node = new_node
    
    def insert_after(self, node, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        temp_node = self.head_node
        while temp_node.data is not node:
            temp_node = temp_node.next_node
            if temp_node.next_node is None:
                break
        new_node.next_node = temp_node.next_node
        temp_node.next_node = new_node
    
    
    def traverse(self):
        current_node = self.head_node
        while current_node is not None:
            print(current_node)
            current_node = current_node.next_node
            
    def add(self, node):
        self.num_of_nodes += 1
        new_node = Node(node)
        if self.head_node is None:
            self.head_node = new_node
        elif self.head_node.data.title > new_node.data.title:
            new_node.next_node = self.head_node
            self.head_node = new_node
        else:
            temp_node = self.head_node
            previous_node = self.head_node
            while temp_node.data.title < new_node.data.title:
                previous_node = temp_node
                temp_node = temp_node.next_node
                if temp_node.next_node is None:
                    break
            previous_node.next_node = new_node
            new_node.next_node = temp_node
    
    def search(self, keyword):
        matches = []
        current_node = self.head_node
        while current_node is not None:
            if keyword.upper() in current_node.data.title or keyword.upper() in current_node.data.author.upper():
                matches.append(current_node)
            current_node = current_node.next_node
        return matches
    
    def update_inventory(self):
        print("Enter keyword: ")
        search = input()
        matches = self.search(search)
        book_numbers = []
        for i in range(len(matches)):
            book_numbers.append(f"{i+1}. {matches[i]}")
        for i in range(len(book_numbers)):
            print (f"{book_numbers[i]}")
        print()
        if len(matches) == 0:
            print("No results found. Please try again.")
            return
        print("Enter the number that corresponds to the book you want to check in/out: ")
        index = input()
        index = int(index)
        print()
        print("Would you like to return this book (1) or check it out (2)? ")
        status = input()
        status = int(status)
        temp_node = self.head_node
        while temp_node.data is not matches[index - 1]:
            temp_node = temp_node.next_node
            if temp_node.next_node is None:
                break
        if status == 1:
            print(f"You returned {matches[index - 1]}!")
            temp_node.data.in_stock = True
        else:
            if (temp_node.data.in_stock == True):
                print()
                print(f"You checked out {matches[index - 1]}!")
                temp_node.data.in_stock = False
                print()
            else:
                print()
                print("This book is out of stock. Come back soon to check availability.")
                print()
        
class Book:
    
    all_books = LinkedList()

    def __init__(self, publisher, author, ISBN, date, title, weeks_on_list):
        self.publisher = publisher
        self.author = author
        self.title = title
        self.ISBN = ISBN
        self.date = date
        self.weeks_on_list = weeks_on_list
        self.in_stock = True
        Book.all_books.add(self)
        
    def __repr__(self):
        return f"{self.title} by {self.author.upper()}"
  
    @staticmethod
    def import_books():   
        book_file = open('books.csv')
        for row in book_file:
                line = row.split(",")
                Book(line[1], line[2], line[3], line[4], line[5], line[6])
            
if __name__ == '__main__':
    
    #my_list = LinkedList()
    #user1 = User("Nick Jones", "nick@yahoo.com", "abcABC123")
    #user2 = User("Jonny Jane", "jonny@gmail.com", "aaAA123")
    #user3 = User("Timmy Groves", "timmy@aol.com", "aA123")
    #user4 = User("Nikolozi Khucesvelli", "nikiscool@aol.com", "aA1oei3")
    #my_list.insert_at_start(user1)
    #my_list.insert_at_start(user2)
    #my_list.insert_at_end(user3)
    #my_list.insert_after(user1, user4)
    #my_list.traverse()
    
    Book.import_books()
    #Book.all_books.traverse()
    Book.all_books.update_inventory()
    
    
    
        