from types import FunctionType
a = (x for x in [1])

a = type(a)
print(type(a) is FunctionType)
