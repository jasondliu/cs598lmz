fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #10
def f():
    yield

f().__next__()

# Issue #11
def f():
    return
    yield

f().__next__()

# Issue #12
def f():
    yield
    return

f().__next__()

# Issue #13
def f():
    yield
    yield

f().__next__()

# Issue #14
def f():
    yield
    yield
    return

f().__next__()

# Issue #15
def f():
    yield
    yield
    yield

f().__next__()

# Issue #16
def f():
    yield
    yield
    yield
    return

f().__next__()

# Issue #17
def f():
    yield
    yield
    yield
    yield

f().__next__()

# Issue #18
def f():
    yield
    yield
    yield
    yield
    return

f().__next__()

# Issue #19
def f():
