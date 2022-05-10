from types import FunctionType
a = (x for x in [1])
b = lambda x: x + 1
print(a, b)
print(type(a), type(b), type(FunctionType))

print(isinstance(a, GeneratorType))
print(isinstance(b, FunctionType))

print(isinstance(b, FunctionType))
