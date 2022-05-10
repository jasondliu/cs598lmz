fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22
def f():
    def g():
        yield
    return g

f()()

# Issue #23
def f():
    def g():
        yield
    return g()

f()

# Issue #24
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #25
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #26
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #27
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #28
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #29
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #30
def f():
