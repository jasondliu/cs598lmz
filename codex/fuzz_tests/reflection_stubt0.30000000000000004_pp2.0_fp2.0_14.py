fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #28
def f():
    return f.__code__
f()

# Issue #30
def f():
    return f.__code__.co_code
f()

# Issue #31
def f():
    return f.__code__.co_consts
f()

# Issue #32
def f():
    return f.__code__.co_filename
f()

# Issue #33
def f():
    return f.__code__.co_firstlineno
f()

# Issue #34
def f():
    return f.__code__.co_flags
f()

# Issue #35
def f():
    return f.__code__.co_freevars
f()

# Issue #36
def f():
    return f.__code__.co_lnotab
f()

# Issue #37
def f():
    return f.__code__.co_name
f()

# Issue #38
def f():
    return f.__code__.co_names
