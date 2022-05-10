fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #20
def f():
    def g():
        return 1
    return g

f()()

# Issue #21
def f():
    def g():
        return 1
    return g

f()()

# Issue #22
def f():
    def g():
        return 1
    return g

f()()

# Issue #23
def f():
    def g():
        return 1
    return g

f()()

# Issue #24
def f():
    def g():
        return 1
    return g

f()()

# Issue #25
def f():
    def g():
        return 1
    return g

f()()

# Issue #26
def f():
    def g():
        return 1
    return g

f()()

# Issue #27
def f():
    def g():
        return 1
    return g

f()()

# Issue #28
def f():
    def g():
        return 1
    return g

f
