from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(FunctionType)
print(type(a.__next__))
