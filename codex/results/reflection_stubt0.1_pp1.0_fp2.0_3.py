fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #15
def f():
    def g():
        return 1
    return g

f()()

# Issue #16
def f():
    def g():
        return 1
    return g

f()()

# Issue #17
def f():
    def g():
        return 1
    return g

f()()

# Issue #18
def f():
    def g():
        return 1
    return g

f()()

# Issue #19
def f():
    def g():
        return 1
    return g

f()()

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

f
