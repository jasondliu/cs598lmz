from types import FunctionType
a = (x for x in [1])
print(type(a))
print(FunctionType)
print(type(a) is FunctionType)
