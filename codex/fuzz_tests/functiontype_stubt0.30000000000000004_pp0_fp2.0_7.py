from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(a) == type(b) == FunctionType)
print(type(a) is type(b) is FunctionType)
print(type(a) == type(b) == FunctionType == type(lambda: None))
print(type(a) is type(b) is FunctionType is type(lambda: None))

print(type(a) == type(b) == FunctionType == type(lambda: None) == type(map))
print(type(a) is type(b) is FunctionType is type(lambda: None) is type(map))

print(type(a) == type(b) == FunctionType == type(lambda: None) == type(map) == type(filter))
print(type(a) is type(b) is
