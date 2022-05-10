from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a))
print(type(b))
print(isinstance(b, list))
print(type(b) is list)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(type(a) is GeneratorType)
print(type(a) is FunctionType)

print('--------------------------------')

class A():
    def __init__(self):
        self.n = 2

    def add(self, m):
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        self.n += m

a = A()
b = B()

print(a.n)
print(b.n)
print(b.n)

print('--------------------------------')

class C():
    def __init__(self, size=10):
        self.size = size
    def getsize(self):
        return self.size
    def setsize(
