fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ attribute of a built-in function should be read-only
def f():
    pass
f.__code__ = None

# Issue #24071: __code__ attribute of a built-in function should be read-only
def f():
    pass
f.__code__ = None

# Issue #24071: __code__ attribute of a built-in function should be read-only
def f():
    pass
f.__code__ = None

# Issue #24071: __code__ attribute of a built-in function should be read-only
def f():
    pass
f.__code__ = None

# Issue #24071: __code__ attribute of a built-in function should be read-only
def f():
    pass
f.__code__ = None

# Issue #24071: __code__ attribute of a built-in function should be read-only
def f():
    pass
f.__code__ = None

# Issue #24071: __code__ attribute of a built
