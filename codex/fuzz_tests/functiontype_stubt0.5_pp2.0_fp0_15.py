from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(lambda x: x))
print(type(FunctionType))

print(isinstance(a, GeneratorType))
print(isinstance(a.__next__, FunctionType))
print(isinstance(a.__iter__, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(FunctionType, type))
