from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))

b = (x for x in [1])
print(isinstance(b, FunctionType))
