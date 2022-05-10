from types import FunctionType
a = (x for x in [1])
print(type(a))
b = (x for x in [1])
print(type(b))
print(isinstance(a, type(b)))
print(isinstance(b, FunctionType))
