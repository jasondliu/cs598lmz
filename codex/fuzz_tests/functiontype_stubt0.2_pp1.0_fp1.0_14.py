from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(FunctionType == FunctionType)
print(FunctionType is FunctionType)
print(type(FunctionType) == type(FunctionType))
print(type(FunctionType) is type(FunctionType))
print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))
print(type(FunctionType) == type(a))
print(type(FunctionType) is type(a))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(b) == type(a))
print(type(b) is type(a))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(b) == type(a))
print(type(b) is type(a))
print(type(a) == type(b))
