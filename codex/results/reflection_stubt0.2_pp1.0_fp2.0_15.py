fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #13
def f():
    return f
f.__code__ = f
f()

# Issue #14
def f():
    return f
f.__code__ = f
f()

# Issue #15
def f():
    return f
f.__code__ = f
f()

# Issue #16
def f():
    return f
f.__code__ = f
f()

# Issue #17
def f():
    return f
f.__code__ = f
f()

# Issue #18
def f():
    return f
f.__code__ = f
f()

# Issue #19
def f():
    return f
f.__code__ = f
f()

# Issue #20
def f():
    return f
f.__code__ = f
f()

# Issue #21
def f():
    return f
f.__code__ = f
f()

# Issue #22
def f():
    return f
f.__code__ = f
f()
