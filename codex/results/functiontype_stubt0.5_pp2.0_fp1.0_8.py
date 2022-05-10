from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(lambda x: x))
print(isinstance(lambda x: x, FunctionType))
