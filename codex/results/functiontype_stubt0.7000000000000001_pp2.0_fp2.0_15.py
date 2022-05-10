from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a)) # <class 'generator'>
print(isinstance(a, FunctionType)) # False
