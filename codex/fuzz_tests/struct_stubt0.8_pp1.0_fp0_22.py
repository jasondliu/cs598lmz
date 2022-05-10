from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.pack(123)

# __new__(cls, fmt)
from _struct import _clearcache
from random import random
def gen(n):
    for i in xrange(n):
        yield int(random() * 32767)
from timeit import timeit
print(timeit('list(gen(1000))', 'from __main__ import gen', number=10000))
c = []
print(timeit('c.extend(gen(1000))', 'from __main__ import gen, c', number=10000))
_clearcache()

# __new__(cls, fmt)
from _struct import Struct
from timeit import timeit
s = Struct.__new__(Struct)
s.__init__('>H')
print(timeit('s.pack(123)', 'from __main__ import s', number=10000))
_clearcache()

# __new__(cls, fmt)
from _struct import Struct
from timeit import timeit
Struct.__new__(Struct, '>
