from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)

print(type(a))
print(type(b))

print(type(FunctionType))
print(type(a) == FunctionType)
print(type(b) == FunctionType)

print(type(a) == type(b))

print(type(a) == type(b) == FunctionType)

print(type(a) == type(b) == type(FunctionType))

print(type(a) == type(b) == type(FunctionType) == FunctionType)

print(type(a) == type(b) == type(FunctionType) is FunctionType)

print(type(a) == type(b) == type(FunctionType) == type(FunctionType))

print(type(a) == type(b) == type(FunctionType) is type(FunctionType))

print(type(a) == type(b) == type(FunctionType) == type(FunctionType) is FunctionType)

print(type(a) == type
