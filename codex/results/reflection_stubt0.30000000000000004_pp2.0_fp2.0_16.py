fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #14
def f():
    def g():
        pass
    g.__code__ = 42
    return g
f()()

# issue #15
def f():
    def g():
        pass
    g.__code__ = g
    return g
f()()

# issue #16
def f():
    def g():
        pass
    g.__code__ = f
    return g
f()()

# issue #17
def f():
    def g():
        pass
    g.__code__ = f.__code__
    return g
f()()

# issue #18
def f():
    def g():
        pass
    g.__code__ = f.__code__.__code__
    return g
f()()

# issue #19
def f():
    def g():
        pass
    g.__code__ = f.__code__.__code__.__code__
    return g
f()()

# issue #20
def f():
    def g():

