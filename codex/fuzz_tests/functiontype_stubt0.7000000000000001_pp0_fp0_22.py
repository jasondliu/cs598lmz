from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(FunctionType == FunctionType)
print(type(a) == type(b))

class A(object):
    pass

class B(object):
    pass

print(A == B)
print(type(A) == type(B))

print(type(1))
print(type("a"))
print(type(FunctionType))
print(type(A))
print(type(a))

print(type(1) == int)
print(type("a") == str)
print(type(FunctionType) == FunctionType)
print(type(A) == A)
print(type(a) == type(b))

print(type(1) == int())
print(type("a") == str())
print(type(FunctionType) == FunctionType())
print(type(A) == A())
print(type(a) == type(b)())

print(type(1) is int)
print(type("a") is str)
print(type(FunctionType
