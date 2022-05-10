from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(isinstance(a, Iterator) and isinstance(a, Iterable))
print(isinstance(a, Iterator) or isinstance(a, Iterable))

print(issubclass(Iterator, Iterable))
print(issubclass(Iterator, Iterator))
print(issubclass(Iterator, GeneratorType))
print(issubclass(Iterator, FunctionType))

print(issubclass(GeneratorType, Iterable))
print(issubclass(GeneratorType, Iterator))
print(issubclass(GeneratorType, GeneratorType))
print(issubclass(GeneratorType, FunctionType))

print(issubclass(FunctionType, Iterable))
print(issubclass(FunctionType, Iterator))
print(issubclass(FunctionType, GeneratorType))
print(issubclass(FunctionType, FunctionType))
