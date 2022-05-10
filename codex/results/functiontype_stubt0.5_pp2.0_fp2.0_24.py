from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = a
print(a == b)
print(a == c)
print(b == c)
print(a is b)
print(a is c)
print(b is c)
print(type(a) is type(b))
print(type(a) is type(c))
print(type(b) is type(c))
print(type(a) is FunctionType)
print(type(b) is FunctionType)
print(type(c) is FunctionType)

print()

a = (x for x in [1])
b = (x for x in [1])
c = a
print(a == b)
print(a == c)
print(b == c)
print(a is b)
print(a is c)
print(b is c)
print(type(a) is type(b))
print(type(a) is type(c))
print(type(b) is type(c))
print(type(a) is FunctionType)
print(type(b) is Function
