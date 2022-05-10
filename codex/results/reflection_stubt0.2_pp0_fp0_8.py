fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #28
def f():
    def g():
        yield
    return g

f()()

# Issue #29
def f():
    def g():
        yield
    return g()

f()

# Issue #30
def f():
    def g():
        yield
    return g()

f()

# Issue #31
def f():
    def g():
        yield
    return g()

f()

# Issue #32
def f():
    def g():
        yield
    return g()

f()

# Issue #33
def f():
    def g():
        yield
    return g()

f()

# Issue #34
def f():
    def g():
        yield
    return g()

f()

# Issue #35
def f():
    def g():
        yield
    return g()

f()

# Issue #36
def f():
    def g():
        yield
    return g()

f()

# Issue #37

