fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16095: test that a generator with a non-tuple code object
# raises a TypeError.
def f():
    yield 1
fn = lambda: None
fn.__code__ = f.__code__
try:
    fn()
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue #16095: test that a generator with a non-tuple code object
# raises a TypeError.
def f():
    yield 1
fn = lambda: None
fn.__code__ = f.__code__
try:
    fn()
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue #16095: test that a generator with a non-tuple code object
# raises a TypeError.
def f():
    yield 1
fn = lambda: None
fn.__code__ = f.__code__
try:
    fn()
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue
