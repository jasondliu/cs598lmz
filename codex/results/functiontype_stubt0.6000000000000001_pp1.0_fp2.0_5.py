from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == type(lambda x: x))

from collections import Iterable
from collections import Iterator
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

print(isinstance(a, (GeneratorType, FunctionType)))

print(isinstance(a, (GeneratorType, FunctionType, Iterable)))

print(isinstance(a, (GeneratorType, FunctionType, Iterable, Iterator)))

print(isinstance(a, (GeneratorType, FunctionType, Iterable, Iterator, object)))
