from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) == a)
print(type(a.__iter__()) == a.__iter__)


x = "asdf"
print(type(x.__add__))
print(type(x.__add__) == FunctionType)
print(type(x.__add__))
print(type(x.__add__) == x.__add__)
print(x.__add__("asdf"))

class X:
    def __init__(self):
        print("X")
        self.x = [self]
        self.y = [self]

print(type(X.__init__))
print(X.__init__ == X)
print(type(X.__init__) == X)
print(type(X.__init__) == X.__init__)
print(type(X.__init__) == FunctionType)
print(X.__init__ == FunctionType)
x = X()
print(type(
