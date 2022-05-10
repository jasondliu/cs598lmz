fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #4639: check for refleaks on generators

def f():
    yield 1
    raise StopIteration
    yield 2

for i in range(10000):
    f()

# Issue #12691: check that generators restore the exception state
# properly when re-raising StopIteration.

def g():
    yield 1
    try:
        raise ValueError
    except:
        yield 2
    yield 3

l = list(g())
try:
    next(g())
except ValueError:
    pass
else:
    raise RuntimeError("should raise ValueError")

# Issue #16300: check that generators don't leak when used as an iterator

def f():
    yield 1
    raise StopIteration
    yield 2

def g():
    yield 1
    raise RuntimeError
    yield 2

class C(object):
    def __iter__(self):
        yield 1
        raise StopIteration
        yield 2

for f in (f, g, C):
    for i in range(10000):

