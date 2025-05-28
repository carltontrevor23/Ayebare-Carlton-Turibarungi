class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # Inherits from B and C
    pass

d = D()
d.show() 

print(D.mro())  
