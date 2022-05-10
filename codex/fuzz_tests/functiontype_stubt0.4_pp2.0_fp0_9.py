from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

print(a is b)

print(type(a) == type(b))

print(isinstance(a, type(b)))

print(isinstance(a, FunctionType))

print(isinstance(a, GeneratorType))

print(isinstance(a, IteratorType))

print(isinstance(a, IterableType))

print(isinstance(a, object))

print(isinstance(a, (list, tuple)))

print(isinstance(a, (list, tuple, dict)))

print(isinstance(a, (list, tuple, dict, GeneratorType)))

print(isinstance(a, (list, tuple, dict, GeneratorType, FunctionType)))

print(isinstance(a, (list, tuple, dict, GeneratorType, FunctionType, IterableType)))

print(isinstance(a, (list, tuple, dict, GeneratorType, FunctionType, IterableType, IteratorType)))

print(isinstance(a, (list, tuple, dict
