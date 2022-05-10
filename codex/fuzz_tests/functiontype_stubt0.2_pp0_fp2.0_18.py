from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == type(a.__iter__))

print("-"*50)

class A:
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self
    def __next__(self):
        return self.x

a = A(1)
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == type(a.__iter__))

print("-"*50)

class A:
    def __init__(self, x):
        self.x =
