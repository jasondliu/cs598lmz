fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash
def f():
    yield

f().__next__()

# This should not crash

