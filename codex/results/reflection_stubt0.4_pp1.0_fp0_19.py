fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn()

# The following should not raise an exception
def f():
    def g():
        pass
    g.__code__ = None
    return g

f()()

# The following should not raise an exception
def f():
    def g():
        pass
    g.__code__ = 42
    return g

f()()

# The following should not raise an exception
def f():
    def g():
        pass
    g.__code__ = 'abc'
    return g

f()()

# The following should not raise an exception
def f():
    def g():
        pass
    g.__code__ = object()
    return g

f()()

# The following should not raise an exception
def f():
    def g():
        pass
    g.__code__ = f
    return g

f()()

# The following should not raise an exception
def f():
    def g():
        pass
    g.__code__ = f.__
