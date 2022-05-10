fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16
def f():
    yield

f().__next__()

# Issue #17
def f():
    yield

f().__iter__()

# Issue #18
def f():
    yield

f().__length_hint__()

# Issue #19
def f():
    yield

f().__await__()

# Issue #20
def f():
    yield

f().__aiter__()

# Issue #21
def f():
    yield

f().__anext__()

# Issue #22
def f():
    yield

f().__aenter__()

# Issue #23
def f():
    yield

f().__aexit__()

# Issue #24
def f():
    yield

f().__aiter__().__anext__()

# Issue #25
def f():
    yield

f().__aiter__().__aenter__()

# Issue #26
def f():
    yield

f().__aiter
