from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == tuple)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, tuple))

print(isinstance(a, (GeneratorType, FunctionType, tuple)))

print('----------')

print(issubclass(GeneratorType, FunctionType))
print(issubclass(tuple, FunctionType))
print(issubclass(str, FunctionType))
