from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))

print(isinstance(lambda x: x, FunctionType))

print(isinstance(lambda x: x, FunctionType))
