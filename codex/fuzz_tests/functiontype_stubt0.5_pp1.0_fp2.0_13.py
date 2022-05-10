from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(b, (GeneratorType, FunctionType)))
print(isinstance(c, (GeneratorType, FunctionType)))
