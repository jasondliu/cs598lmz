from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))

print(type(a) == type(lambda x: x))
print(type(a) == type(FunctionType))
print(type(lambda x: x) == type(FunctionType))

print(type(a) == type(FunctionType))
print(type(lambda x: x) == type(FunctionType))

print(type(a) == type(FunctionType))
print(type(lambda x: x) == type(FunctionType))

print(type(a) == type(FunctionType))
print(type(lambda x: x) == type(FunctionType))

print(type(a) == type(FunctionType))
print(type(lambda x: x) == type(FunctionType))

print(type(a) == type(FunctionType))
print(type(lambda x: x) == type(FunctionType))

print(type(a) == type(FunctionType))
print(type(lambda x: x) == type(FunctionType))

print(type
