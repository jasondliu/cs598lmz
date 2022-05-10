fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #15
def f():
    yield

f().__next__()

# Issue #16
def f():
    yield

f().__next__()

# Issue #17
def f():
    yield

f().__next__()

# Issue #18
def f():
    yield

f().__next__()

# Issue #19
def f():
    yield

f().__next__()

# Issue #20
def f():
    yield

f().__next__()

# Issue #21
def f():
    yield

f().__next__()

# Issue #22
def f():
    yield

f().__next__()

# Issue #23
def f():
    yield

f().__next__()

# Issue #24
def f():
    yield

f().__next__()

# Issue #25
def f():
    yield

f().__next__()

# Issue #26
def f():
    yield

f().__next
