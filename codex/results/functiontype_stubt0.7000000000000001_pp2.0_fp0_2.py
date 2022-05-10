from types import FunctionType
a = (x for x in [1])
b = [1]
c = 1
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))
