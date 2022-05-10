from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(a)
print(type(a))
print(type(b))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
