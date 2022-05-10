from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, list))
print(isinstance(a, tuple))
