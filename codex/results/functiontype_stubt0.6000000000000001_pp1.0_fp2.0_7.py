from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)

print(type(a) is FunctionType)
print(type(b) is FunctionType)

print(type(a) == FunctionType)
print(type(b) == FunctionType)

print(type(a) is type(b))
print(type(a) == type(b))

print(type(a) is type(lambda: 1))
print(type(b) is type(lambda: 1))

print(type(a) == type(lambda: 1))
print(type(b) == type(lambda: 1))
