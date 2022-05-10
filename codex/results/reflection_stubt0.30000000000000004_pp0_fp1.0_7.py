fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #28
def f():
    yield
f.__code__ = None
f()

# Issue #29
def f():
    yield
f.__code__ = f
f()

# Issue #30
def f():
    yield
f.__code__ = f.__code__
f()

# Issue #31
def f():
    yield
f.__code__ = f.__code__.__code__
f()

# Issue #32
def f():
    yield
f.__code__ = f.__code__.__code__.__code__
f()

# Issue #33
def f():
    yield
f.__code__ = f.__code__.__code__.__code__.__code__
f()

# Issue #34
def f():
    yield
f.__code__ = f.__code__.__code__.__code__.__code__.__code__
f()

# Issue #35
def f():
    yield
f.__code__ = f.
