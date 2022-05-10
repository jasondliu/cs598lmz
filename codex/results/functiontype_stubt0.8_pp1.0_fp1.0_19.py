from types import FunctionType
a = (x for x in [1])
b = FunctionType
print(type(a) is b, a)
