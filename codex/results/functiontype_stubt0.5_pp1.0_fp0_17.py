from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(FunctionType(a) is FunctionType(b))
