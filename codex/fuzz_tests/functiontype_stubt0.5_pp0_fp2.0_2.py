from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a))
print(type(b))
print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(a.__next__())

def add(a, b):
    return a + b

print(type(add))
print(isinstance(add, FunctionType))
print(isinstance(add, object))
print(isinstance(add, int))

class A(object):
    pass

a = A()
print(type(A))
print(isinstance(a, A))
print(isinstance(a, object))
print(isinstance(a, int))

class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "A(%s, %s)" % (self.a, self.b)

a = A(1, 2)
print(a)
print(str(a
