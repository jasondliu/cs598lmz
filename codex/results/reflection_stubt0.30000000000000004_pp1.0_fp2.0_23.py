fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #11893: segfault when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #11893: segfault when __code__ is a generator
def f():
    yield
f.__code__ = f
f()

# Issue #11893: segfault when __code__ is a generator
def f():
    yield
f.__code__ = f.__code__
f()

# Issue #11893: segfault when __code__ is a generator
def f():
    yield
f.__code__ = f.__code__()
f()

# Issue #11893: segfault when __code__ is a generator
def f():
    yield
f.__code__ = f.__code__.__code__
f()

# Issue #11893: segfault when __code__ is a generator
def f():
    yield
f.__code__ = f.__code__.__code__()
f()

