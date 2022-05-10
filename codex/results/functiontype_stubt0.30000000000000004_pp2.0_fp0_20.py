from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a == b)
print(a is b)
print(a)
print(b)

print(type(a) == type(b))
print(type(a) is type(b))
print(type(a))
print(type(b))

print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(a))
print(type(b))

print(type(a) == type(b) == FunctionType)
print(type(a) is type(b) is FunctionType)
print(type(a))
print(type(b))

print(type(a) == type(b) == type(FunctionType))
print(type(a) is type(b) is type(FunctionType))
print(type(a))
print(type(b))

print(type(a) == type(b) == type(FunctionType) == FunctionType)
print(type(a) is type(b) is type(FunctionType) is FunctionType)
