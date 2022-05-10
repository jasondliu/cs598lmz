fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__.co_varnames

# Test for bug #1433.
def f():
    yield 1
    if 0: yield 2
f.__code__.co_flags & CO_GENERATOR

# Test for bug #1690.
def f(a, b=1, *args, **kwds): pass
def f(a, b=1, *, c, **kwds): pass
def f(a, b=1, *, c='1', **kwds): pass
def f(a, b=1, *, c='1'): pass

# Test for bug #1751.
def f(): pass
f.__code__.co_flags & CO_VARKEYWORDS

# Test for bug #1848.
def f(a, b=1, *c, d): pass
def f(a, b=1, *c): pass
def f(a, b=1, *, c=1, **d): pass
def f(a, b=1, *, c=1): pass

# Test
