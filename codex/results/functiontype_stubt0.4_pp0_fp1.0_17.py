from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))
print(type(a) == type(FunctionType))
print(type(a) == type(FunctionType()))
