from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))

def test_gen():
    for x in [1]:
        yield x
b = test_gen()
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, IteratorType))

from collections import Iterable
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

def add(x, y):
    return x + y
from functools import reduce
c = map(add, [1, 2, 3], [4, 5, 6])
print(c)
print(list(c))
d = reduce(add, [1, 2, 3, 4])
print(d)

from itertools import islice
e = (x for x in range(10))
print(list(islice(e, 2)))
e = (x for x in range(10))
print(list(islice(e,
