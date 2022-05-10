from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(a) == type(b) == FunctionType)
print(type(a) is type(b) is FunctionType)

print(type(a) == type(b) == FunctionType == type(a))
print(type(a) is type(b) is FunctionType is type(a))

print(type(a) == type(b) == FunctionType == type(a) == type(b))
print(type(a) is type(b) is FunctionType is type(a) is type(b))

print(type(a) == type(b) == FunctionType == type(a) == type(b) == FunctionType)
print(type(a) is type(b) is FunctionType is
