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
    yield

f().__next__()
f().__next__()

# Issue #18
def f():
    yield
    yield
    yield

f().__next__()
f().__next__()
f().__next__()

# Issue #19
def f():
    yield
    yield
    yield
    yield

f().__next__()
f().__next__()
f().__next__()
f().__next__()

# Issue #20
def f():
    yield
    yield
    yield
    yield
    yield

f().__next__()
f().__next__()
f().__next__()
f().__next__()
f().__next__()

# Issue #21
def f():
    yield
    yield
    yield
    yield
    yield
    yield

f().__next__()
f().__next__()
f
