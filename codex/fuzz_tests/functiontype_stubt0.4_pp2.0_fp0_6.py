from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a==b)
print(a is b)
print(type(a) is type(b))
print(type(a) == type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(type(a) == FunctionType)
print(type(b) == FunctionType)
print(type(a))
print(type(b))
print(type(a) is type(b))
print(type(a) == type(b))
print(type(a) is FunctionType)
print(type(b) is FunctionType)
print(type(a) == FunctionType)
print(type(b) == FunctionType)
print(type(a) is type)
print(type(b) is type)
print(type(a) == type)
print(type(b) == type)
print(type(a) is type(type))
print(type(b) is type(type))
print(type(a) == type(type))
print(type
