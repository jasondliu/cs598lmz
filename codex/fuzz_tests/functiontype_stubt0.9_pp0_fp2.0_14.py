from types import FunctionType
a = (x for x in [1])
print(type(lambda a: a))
print(isinstance(a, FunctionType))
