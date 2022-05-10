fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #28
def f():
    yield

f().__next__()

# Issue #29
def f():
    yield

f().__iter__()

# Issue #30
def f():
    yield

f().__length_hint__()

# Issue #31
def f():
    yield

f().__await__()

# Issue #32
def f():
    yield

f().__aiter__()

# Issue #33
def f():
    yield

f().__anext__()

# Issue #34
def f():
    yield

f().__aenter__()

# Issue #35
def f():
    yield

f().__aexit__()

# Issue #36
def f():
    yield

f().__anext__()

# Issue #37
def f():
    yield

f().__aenter__()

# Issue #38
def f():
    yield

f().__aexit__()

# Issue #39
def
