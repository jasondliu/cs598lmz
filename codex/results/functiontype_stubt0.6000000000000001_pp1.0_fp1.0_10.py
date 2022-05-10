from types import FunctionType
a = (x for x in [1])
print(type(a))

def b():
    yield 1
print(type(b))
print(type(b()))

class A:
    def __init__(self):
        self.x = 1
a = A()
print(type(a))

class B:
    def __init__(self):
        self.x = 1
    def __call__(self):
        return self.x
b = B()
print(type(b))
print(type(b()))

class C:
    def __init__(self):
        self.x = 1
    def __call__(self):
        return self.x
c = C()
print(type(c))
print(type(c()))

class D:
    def __init__(self):
        self.x = 1
    def __call__(self):
        return self.x
d = D()
print(type(d))
print(type(d()))

class E:
    def __init__(self):
        self.x = 1
   
