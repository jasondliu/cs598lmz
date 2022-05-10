from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(a, (GeneratorType, FunctionType, Iterator)))
print(isinstance(a, (GeneratorType, FunctionType, Iterator, Iterable)))

print(isinstance(a, (FunctionType, Iterator, Iterable)))
print(isinstance(a, (FunctionType, Iterator)))
print(isinstance(a, (FunctionType, Iterable)))

print(isinstance(a, (Iterator, Iterable)))
print(isinstance(a, (Iterator)))
print(isinstance(a, (Iterable)))

print(isinstance(a, (FunctionType, Iterator, Iterable, GeneratorType)))
print(isinstance(a, (FunctionType, Iterator, Iterable, GeneratorType, int)))
print(isinstance(a, (FunctionType, Iterator
