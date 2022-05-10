fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #11
def f():
    def g():
        pass
    g.__code__ = g

# Issue #12
def f():
    def g():
        pass
    g.__code__ = f

# Issue #13
def f():
    def g():
        pass
    g.__code__ = f.__code__

# Issue #14
def f():
    def g():
        pass
    g.__code__ = f.__code__.__code__

# Issue #15
def f():
    def g():
        pass
    g.__code__ = f.__code__.__code__.__code__

# Issue #16
def f():
    def g():
        pass
    g.__code__ = f.__code__.__code__.__code__.__code__

# Issue #17
def f():
    def g():
        pass
    g.__code__ = f.__code__.__code__.__code__.__code__.__code__

