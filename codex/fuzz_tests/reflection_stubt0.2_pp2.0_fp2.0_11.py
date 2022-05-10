fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23
def f():
    yield
    yield
    yield

f.__code__ = f
f()

# Issue #24
def f():
    yield
    yield
    yield

f.__code__ = f.__code__
f()

# Issue #25
def f():
    yield
    yield
    yield

f.__code__ = f.__code__
f()

# Issue #26
def f():
    yield
    yield
    yield

f.__code__ = f.__code__
f()

# Issue #27
def f():
    yield
    yield
    yield

f.__code__ = f.__code__
f()

# Issue #28
def f():
    yield
    yield
    yield

f.__code__ = f.__code__
f()

# Issue #29
def f():
    yield
    yield
    yield

f.__code__ = f.__code__
f()

# Issue #30
def f
