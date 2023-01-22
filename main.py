bc=""
class library:

    def __init__(self,lst):
        self.books=lst

    def dspavailablebooks(self):
        print("books available are")
        for book in self.books:
            print(" \t"+book)

    def borrow(self,bookname):
        if bookname in self.books:
            print(f"You have been issued book {bookname}")
            (self.books).remove(bookname)
            global bc
            bc=bookname
            return True
        else:
            print("This book isn't available right now.")
            return False

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thans for keeping it safe")


class student:
    def __init__(self):
        self.borrowed=[]

    def borrow(self):
        req=input("Enter book name:-")
        return req
    
    def returns(self):
        req=input("Enter book name:-")
        # (self.borrowed).remove(req)
        return req 

    def borrowadd(self,bookname):
        self.borrowed.append(bookname)


if __name__=="__main__":
    cntlib=library(["Python","Java","C++","C#"])

    while True:
        print("welcome to central library")
        cntlib.dspavailablebooks()

        user=student()

        a=input("To request a book(Borrow) To return a book(Return):-")

        if a.lower()=="borrow":
            cntlib.borrow(user.borrow())
            user.borrowadd(bc)
        elif a.lower()=="return":
            cntlib.returnbook(user.returns())
        else:
            print("Invalid choice")
        print("\n\n")