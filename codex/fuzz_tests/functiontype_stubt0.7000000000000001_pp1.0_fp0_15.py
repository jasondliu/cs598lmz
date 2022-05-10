from types import FunctionType
a = (x for x in [1])
isinstance(a, Iterator)

b = [1,2]
c = (1,2)
d = {'a':1, 'b':2}
e = {1,2}
f = FunctionType

print(isinstance(b, Iterable), isinstance(c, Iterable), isinstance(d, Iterable), isinstance(e, Iterable), isinstance(f, Iterable))
print(isinstance(b, Iterator), isinstance(c, Iterator), isinstance(d, Iterator), isinstance(e, Iterator), isinstance(f, Iterator))

from collections import Iterable
from collections import Iterator

c = (1,2,3,4)
print(isinstance(c, Iterable), isinstance(c, Iterator))
print(isinstance(iter(c), Iterable), isinstance(iter(c), Iterator))

def g():
    yield 1
    yield 2

print(isinstance(g(), Iterator))

from collections import Iterable

b = [1,2,3,4]
c
