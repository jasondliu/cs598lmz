from types import FunctionType
a = (x for x in [1])
# a = []
# b = a.__class__
# print(b.f)
# print(FunctionType)
# print(FunctionType.mro)
print(type(None))
print(type(a))

import collections
from sys import getrefcount
b = []
a = [[]]
print(a)
print(getrefcount(a))
a[0].append(b)
b.append(a)
# print(getrefcount(a))

print(collections.namedtuple(None, [1, 2, 3]))
