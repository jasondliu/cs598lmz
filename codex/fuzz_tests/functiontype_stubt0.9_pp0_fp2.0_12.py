from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(a) == type(abs))
