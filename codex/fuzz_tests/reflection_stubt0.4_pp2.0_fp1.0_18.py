fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #9190: segfault when assigning to __code__
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f()

# Issue #9190: segfault when assigning to __code__
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f.__code__ = f.__code__
f()

# Issue #9190: segfault when assigning to __code__
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f.__code__ = f.__code__
f.__code__ = g.__code__
f()

# Issue #9190: segfault when assigning to __code__
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f.__code__ = f.__code__
f.__code__ = g.__code__
f.__code
