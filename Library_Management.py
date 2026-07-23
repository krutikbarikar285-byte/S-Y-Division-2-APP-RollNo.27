class Library:
    def __init__(self):
        self.books=["python","java","c++"]
        
    def borrow(self,book):
        if book in self.books:
            self.books.remove(book)
            print("Book Borrowed")
        else:
            print("Book Not Available")
            
    def return_book(self,book):
        self.books.append(book)
        print("Book Returned")
        
    def display(self):
        print(self.books)
library=Library()

while True:
  print("\n1.Display Books")
  print("2.Borrow Book")      
  print("3.Return Book")
  print("4.Exit")
  
  choice=int(input("Enter your choice:"))
  
  if choice==1:
      library.display()
  elif choice==2:
      book=input("Enter book name:")
      library.borrow(book)
  elif choice==3:
      book=input("Enter book name:")
      library.return_book(book)
  elif choice==4:
      print("Thank you!")
      break
  else:
      print("invalid choice")                 
