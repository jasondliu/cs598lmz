from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type([1]))
print(type(1))
print(type(FunctionType))
print(type(lambda a: a + 1))
print(type(a))
print(type(a))
print(type(a))
print(type(a))

class A:
    def __init__(self):
        pass


print(type(A))
print(type(A()))

class B(A):
    def __init__(self):
        pass


print(type(B))
print(type(B()))

print(type(A()))


class C(A):
    def __init__(self):
        pass


print(type(C))
print(type(C()))

class D(B, C):
    def __init__(self):
        pass


print(type(D))
print(type(D()))


print(D.__mro__)
print(D.__mro__[0])
print(D.__mro__[1])

