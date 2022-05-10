from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(type(a))
print(type(b))

print(type(FunctionType))

print(type(FunctionType) == FunctionType)

print(type(type) == type)

print(type(type))

print(type(type) == FunctionType)

print(type(type) == type)

print(type(type) == FunctionType)
