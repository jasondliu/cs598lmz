from types import FunctionType
a = (x for x in [1])
b = FunctionType.__call__(lambda: x, ())
print(a)
print(b)
if b is a:
    print('Yes')
else:
    print('No')

c = iter(b)
try:
    print(next(c))
except StopIteration:
    print('Empty')
"""

"""
from types import FunctionType
a = (x for x in [1])
b = FunctionType.__call__(lambda: x, ())
print(a)
print(b)
print(a is b)

c = iter(b)
print(next(c), next(c), next(c), next(c), next(c))
"""

"""
from types import FunctionType
a = (x for x in [1, 2, 3])
b = FunctionType.__call__(lambda: next(a), ())
print(a)
print(b)
if b is a:
    print('Y')
else:
    print('N')
print(a)
print(b)
if b is a:
    print
