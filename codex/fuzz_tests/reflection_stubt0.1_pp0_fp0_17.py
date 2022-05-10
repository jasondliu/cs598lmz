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
    yield 1
    yield 2

f().__next__()
f().__next__()

# Issue #17
def f():
    yield 1
    yield 2

f().__next__()
f().__next__()

# Issue #18
def f():
    yield 1
    yield 2

f().__next__()
f().__next__()

# Issue #19
def f():
    yield 1
    yield 2

f().__next__()
f().__next__()

# Issue #20
def f():
    yield 1
    yield 2

f().__next__()
f().__next__()

# Issue #21
def f():
    yield 1
    yield 2

f().__next__()
f().__next__()

# Issue #22
def f():
    yield 1
    yield 2

f().__next__()
f().__next
