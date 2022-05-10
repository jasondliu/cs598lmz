from types import FunctionType
a = (x for x in [1])
b = (1)
print(type(a))
print(type(b))
print(isinstance(a,FunctionType))
