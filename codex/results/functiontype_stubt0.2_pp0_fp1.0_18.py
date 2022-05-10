from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))

print(isinstance(a, list))
print(isinstance(a, tuple))
print(isinstance(a, dict))
print(isinstance(a, set))

print(isinstance(a, (list, tuple, dict, set)))

print(isinstance(a, (list, tuple, dict, set, GeneratorType)))

print(isinstance(a, (list, tuple, dict, set, GeneratorType, FunctionType)))

print(isinstance(a, (list, tuple, dict, set, GeneratorType, FunctionType, IteratorType)))

print(isinstance(a, (list, tuple, dict, set, GeneratorType, FunctionType, IteratorType, IterableType)))

print(isinstance(a, (list, tuple, dict, set, GeneratorType, FunctionType, IteratorType, IterableType, object)))

print(isinstance(a, (list
