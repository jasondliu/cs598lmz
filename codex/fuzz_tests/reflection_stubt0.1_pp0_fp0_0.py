fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #14095: test that the code object of a generator is not
# freed when the generator is destroyed.
import weakref
def f():
    yield 1
    yield 2
    yield 3
g = f()
next(g)
wr = weakref.ref(g.gi_code)
del g
assert wr() is not None

# Issue #14095: test that the code object of a generator is not
# freed when the generator is destroyed.
import weakref
def f():
    yield 1
    yield 2
    yield 3
g = f()
next(g)
wr = weakref.ref(g.gi_code)
del g
assert wr() is not None

# Issue #14095: test that the code object of a generator is not
# freed when the generator is destroyed.
import weakref
def f():
    yield 1
    yield 2
    yield 3
g = f()
next(g)
wr = weakref.ref(g.gi_code)
del g
assert wr() is not None

# Issue
