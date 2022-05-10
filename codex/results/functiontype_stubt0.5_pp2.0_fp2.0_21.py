from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x + 1))
print(type(FunctionType))
print(FunctionType)

from collections import Iterable
print(isinstance(a, Iterable))
print(isinstance(lambda x: x + 1, Iterable))
print(isinstance(FunctionType, Iterable))

from collections import Iterator
print(isinstance(a, Iterator))
print(isinstance(lambda x: x + 1, Iterator))
print(isinstance(FunctionType, Iterator))

from collections import Generator
print(isinstance(a, Generator))
print(isinstance(lambda x: x + 1, Generator))
print(isinstance(FunctionType, Generator))
