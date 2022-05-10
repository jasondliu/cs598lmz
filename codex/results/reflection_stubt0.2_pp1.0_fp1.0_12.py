fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #15
def f():
    def g():
        yield
    return g()

f().send(None)

# Issue #16
def f():
    def g():
        yield
    return g()

next(f())

# Issue #17
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #18
def f():
    def g():
        yield
    return g()

f().send(None)

# Issue #19
def f():
    def g():
        yield
    return g()

next(f())

# Issue #20
def f():
    def g():
        yield
    return g()

f().__next__()

# Issue #21
def f():
    def g():
        yield
    return g()

f().send(None)

# Issue #22
def f():
    def g():
        yield
    return g()

next(f())

# Issue #23
def
