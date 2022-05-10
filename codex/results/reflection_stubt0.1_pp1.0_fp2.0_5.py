fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

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

f().__next__()

# Issue #27
def f():
    yield

f().__next__()

# Issue #28
def f():
    yield

f().__next__()

# Issue #29
def f():
    yield

f().__next__()

# Issue #30
def f():
    yield

f().__next__()

# Issue #31
def f():
    yield

f().__next
