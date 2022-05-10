from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a) == type(b))
print(type(a))
print(type(b))
print(type(a) == FunctionType)
print(type(b) == FunctionType)
print(type(a) == type(FunctionType))
print(type(b) == type(FunctionType))

print(type(a) == type(lambda x: x))
print(type(b) == type(lambda x: x))
print(type(a) == type(lambda x: x) == type(lambda x: x))
print(type(b) == type(lambda x: x) == type(lambda x: x))

print(type(a) == type(lambda x: x) == type(lambda x: x) == type(lambda x: x))
print(type(b) == type(lambda x: x) == type(lambda x: x) == type(lambda x: x))

print(type(a) == type(lambda x: x) == type(lambda x: x
