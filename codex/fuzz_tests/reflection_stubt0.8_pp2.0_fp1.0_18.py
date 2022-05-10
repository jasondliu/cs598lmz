fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# AttributeError: __code__
# ...
# TypeError: 'generator' object is not callable

# 3.27
import sys
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

s = StringIO()
s.write('hello\n')
sys.stdout = s
print('world')
sys.stdout = sys.__stdout__
print(s.getvalue())

# hello
# world

# 3.28
def multiple(x):
    def F(y):
        return x * y
    return F

print(multiple(3)(9))

# 27

# 3.29

def multiple(x):
    return lambda y: x * y

print(multiple(3)(9))

# 27

# 3.30

from math import sqrt
from functools import reduce
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in is
