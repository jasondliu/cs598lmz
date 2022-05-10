from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a) is FunctionType)
print(type(b) is FunctionType)
print(a is b)

b = (x for x in [1])
print(type(b) is FunctionType)
print(a is b)

c = (x for x in [1])
print(type(c) is FunctionType)
print(a is c)

a = (x for x in [1])
print(type(a) is FunctionType)
print(a is b)
print(a is c)

a = (x for x in [1])
print(type(a) is FunctionType)
print(a is b)
print(a is c)

a = (x for x in [1])
print(type(a) is FunctionType)
print(a is b)
print(a is c)

a = (x for x in [1])
print(type(a) is FunctionType)
print(a is b)
print(a is c)

a = (x for
