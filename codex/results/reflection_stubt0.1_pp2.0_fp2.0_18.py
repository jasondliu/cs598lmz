fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
f.__code__ = None

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to delete __code__ attribute")

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to set __code__ attribute")

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to delete __code__ attribute")

# Issue #23984: __code__ attribute of a function should be read-
