from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(a, (GeneratorType, FunctionType)))

print(isinstance(a, (GeneratorType, FunctionType, list)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, set)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, set, dict)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, set, dict, int)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, set, dict, int, str)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, set, dict, int, str, float)))

print(isinstance(a, (Gener
