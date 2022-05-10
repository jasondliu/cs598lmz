from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(type(b))
print(type(FunctionType))
print(type(type))
print(type(FunctionType) == type(type))

class A:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a

a = A(1)
b = A(1)
c = A(2)
print(a == b)
print(a == c)

class B:
    def __init__(self, a):
        self.a = a

b = B(1)
print(a == b)

class C:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a
    def __ne__(self, other):
        return self.a != other.a

a = C(1)
b = C
