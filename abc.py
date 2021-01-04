class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
     return self.pages+other.pages
c1=book(100)
c2=book(200)
print("the total pages:",c1+c2)