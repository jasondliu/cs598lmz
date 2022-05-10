from types import FunctionType
a = (x for x in [1])
print(type(a))

b = lambda x : x
print(type(b))

c = []
print(type(c))

def d():
    pass

print(type(d))

print(type(abs))

class MyObject(object):
    pass

def fun():
    pass

print(type(fun))
print(type(MyObject))

print(type(lambda x:x))

print(type(x for x in range(10)))

print(type(123))
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == str)
print(type('abc') == type(123))

print(type(b'abc') == bytes)

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print(type(dog))

from types import FunctionType

class MyObject(object):
    def __init__(self):
        self.x
