fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ attribute of a built-in function should be read-only
def f():
    pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in function should be read-only")

# Issue #24071: __code__ attribute of a built-in method should be read-only
def f():
    pass
try:
    f.__call__.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in method should be read-only")

# Issue #24071: __code__ attribute of a built-in method should be read-only
def f():
    pass
try:
    f.__new__.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in method should be read-only")

# Issue #24071: __code__ attribute of a built-
