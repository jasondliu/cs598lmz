fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #27
def f():
    yield

f().__next__()

# issue #28
def f():
    yield
    yield

f().__next__()
f().__next__()

# issue #29
def f():
    yield
    yield
    yield

f().__next__()
f().__next__()
f().__next__()

# issue #30
def f():
    yield
    yield
    yield
    yield

f().__next__()
f().__next__()
f().__next__()
f().__next__()

# issue #31
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

# issue #32
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
