from types import FunctionType
a = (x for x in [1])
print(type(a))

def a():
    pass
print(type(a))
print(type(a) == FunctionType)

class A:
    pass

a = A()
print(type(a))
print(type(a) == A)

print(isinstance(a, A))

print(type(a) == type(A))

print(type(a) == type(1))

print(type(a) == type(1.1))

print(type(a) == type('a'))

print(type(a) == type([]))

print(type(a) == type(()))

print(type(a) == type({}))

print(type(a) == type(None))
