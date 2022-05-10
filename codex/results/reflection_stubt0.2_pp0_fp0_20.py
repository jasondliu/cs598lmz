fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

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
    return g

f()().__next__()

# Issue #28
def f():
    def g():
        yield
    return g

f()().__next__()

# Issue #29
def f():
    def g():
        yield
    return g

f()().__next__()

# Issue #30
def f():
    def g():
        yield
    return g

f()().__next__()

# Issue #31
def f():
    def g():
        yield
    return g

f()().__next__()

# Issue #32
def f():
    def g():
        yield
    return g

f()().__next__()

# Issue #33
def f():
    def g():
        yield
    return g

f()().__next__()


