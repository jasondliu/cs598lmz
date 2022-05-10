fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #10
def f():
    yield
f().__next__()

# issue #11
def f():
    yield
f().__next__()

# issue #12
def f():
    yield
f().__next__()

# issue #13
def f():
    yield
f().__next__()

# issue #14
def f():
    yield
f().__next__()

# issue #15
def f():
    yield
f().__next__()

# issue #16
def f():
    yield
f().__next__()

# issue #17
def f():
    yield
f().__next__()

# issue #18
def f():
    yield
f().__next__()

# issue #19
def f():
    yield
f().__next__()

# issue #20
def f():
    yield
f().__next__()

# issue #21
def f():
    yield
f().__next__()

# issue #22
def f():
