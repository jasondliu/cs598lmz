from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(isinstance(a, Iterator) and isinstance(a, Iterable))

print(isinstance(a, Iterator) or isinstance(a, Iterable))

print(isinstance(a, Iterator) and isinstance(a, Iterable) and isinstance(a, GeneratorType))

print(isinstance(a, Iterator) or isinstance(a, Iterable) or isinstance(a, GeneratorType))

print(isinstance(a, Iterator) and isinstance(a, Iterable) and isinstance(a, GeneratorType) and isinstance(a, FunctionType))

print(isinstance(a, Iterator) or isinstance(a, Iterable) or isinstance(a, GeneratorType) or isinstance(a, FunctionType))

print(isinstance(a, Iterator) and isinstance(a, Iterable) and isinstance(a, GeneratorType)
