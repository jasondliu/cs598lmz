from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) == FunctionType)
print(type(a) == type(b) == FunctionType)
print(type(a) == type(b) == FunctionType == type(a))

print(type(a) == type(b) == FunctionType == type(a) == type(b))

print(type(a) == type(b) == FunctionType == type(a) == type(b) == FunctionType)

print(type(a) == type(b) == FunctionType == type(a) == type(b) == FunctionType == type(a))

print(type(a) == type(b) == FunctionType == type(a) == type(b) == FunctionType == type(a) == type(b))

print(type(a) == type(b) == FunctionType == type(a) == type(b) == FunctionType == type(a) ==
