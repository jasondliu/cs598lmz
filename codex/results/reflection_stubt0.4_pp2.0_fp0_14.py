fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #2800
def f():
    yield

f().__next__()

# Issue #2802
def f():
    yield

f().__next__()

# Issue #2803
def f():
    yield

f().__next__()

# Issue #2804
def f():
    yield

f().__next__()

# Issue #2805
def f():
    yield

f().__next__()

# Issue #2806
def f():
    yield

f().__next__()

# Issue #2807
def f():
    yield

f().__next__()

# Issue #2808
def f():
    yield

f().__next__()

# Issue #2809
def f():
    yield

f().__next__()

# Issue #2810
def f():
    yield

f().__next__()

# Issue #2811
def f():
    yield

f().__next__()

# Issue #2812

