gi = (i for i in ())
# Test gi.gi_code is not None on 3.0, due to a bug.
try:
    next(gi)
except StopIteration:
    pass
else:
    raise AssertionError

def g():
    yield 123

g.gi_frame = None
isinstance(g, types.GeneratorType)

f = lambda: (yield 1)
next(f())

def fn(a, b, c):
    yield a + b + c

g = fn(1, 1, 1)
g.send(None)

try:
    [][0]
except IndexError:
    pass

import sys

def g():
    yield 1
    raise TypeError
    yield 2

try:
    for x in g():
        print(x)
except TypeError:
    exc = sys.exc_info()[1]
    tp = type(exc)
    val = exc.args[0]
    tb = exc.__traceback__
    assert type(tp) is type
    assert type(val) is str
    assert type(tb
