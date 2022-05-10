from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)

print(type(a) == type(b))
print(type(a) is type(b))

print(type(a) == FunctionType)
print(type(a) is FunctionType)

print(type(a) == type(b) == FunctionType)
print(type(a) is type(b) is FunctionType)

print(type(a) == type(b) is FunctionType)
print(type(a) is type(b) == FunctionType)

print(type(a) == type(b) is type(FunctionType))
print(type(a) is type(b) == type(FunctionType))

print(type(a) == type(b) is type(FunctionType) == type(type))
print(type(a) is type(b) == type(FunctionType) is type(type))

print(type(a) == type(b) is type(FunctionType) == type(type) is type)
print(type(
