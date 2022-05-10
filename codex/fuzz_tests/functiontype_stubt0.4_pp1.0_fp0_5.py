from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(a, (GeneratorType, FunctionType)))

print(isinstance(a, (GeneratorType, FunctionType, list)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, int)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, int, dict)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, int, dict, str)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, int, dict, str, set)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, int, dict, str, set, frozenset)))

print(isinstance(a, (GeneratorType, FunctionType, list, tuple, int, dict, str, set, frozenset, object)))


print(
