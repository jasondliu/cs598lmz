fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22652: Test that the code object of a generator is not
# freed when the generator is closed.
import weakref
def g():
    yield 1
    yield 2
    yield 3
g = g()
wr = weakref.ref(g.gi_code)
g.close()
assert wr() is not None

# Issue #22652: Test that the code object of a generator is not
# freed when the generator is exhausted.
def g():
    yield 1
    yield 2
    yield 3
g = g()
wr = weakref.ref(g.gi_code)
list(g)
assert wr() is not None

# Issue #22652: Test that the code object of a generator is not
# freed when the generator is garbage collected.
def g():
    yield 1
    yield 2
    yield 3
wr = weakref.ref(g().gi_code)
del g
assert wr() is not None

# Issue #22652: Test that the code object of a generator is not
# freed when the generator is cleared.
def g
