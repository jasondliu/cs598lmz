from types import FunctionType
a = (x for x in [1])
print(a)
b = list(a)
print(b)

# for i in a:
#     print(i)

def a():
    pass

print(type(a))
print(type(a) == FunctionType)

from collections import Iterable
print(isinstance(a, Iterable))

print(issubclass(FunctionType, type))
print(FunctionType.__mro__)

from collections.abc import Iterable, Iterator
print(isinstance(a, Iterable))
print(issubclass(FunctionType, Iterable))
