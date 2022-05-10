from types import FunctionType
a = (x for x in [1])
b = [1]

print isinstance(a, GeneratorType)
print isinstance(b, GeneratorType)
print isinstance(b, FunctionType)
