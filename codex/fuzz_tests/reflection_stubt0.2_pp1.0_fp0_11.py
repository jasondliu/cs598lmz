fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12079: test that the code object is not modified
# when the generator is closed
def f():
    yield 1
    yield 2
    yield 3

g = f()
c = g.gi_code
g.close()
assert c is g.gi_code

# Issue #12079: test that the code object is not modified
# when the generator is exhausted
g = f()
c = g.gi_code
list(g)
assert c is g.gi_code

# Issue #12079: test that the code object is not modified
# when the generator raises an exception
def f():
    yield 1
    yield 2
    yield 3
    raise ValueError

g = f()
c = g.gi_code
try:
    next(g)
    next(g)
    next(g)
    next(g)
except ValueError:
    pass
assert c is g.gi_code

# Issue #12079: test that the code object is not modified
# when the generator is closed
def f
