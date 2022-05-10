fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18093: __code__ attribute of a function should be read-only
def f():
    pass

try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ = None should have raised TypeError")

# Issue #18093: __code__ attribute of a function should be read-only
def f():
    pass

try:
    del f.__code__
except TypeError:
    pass
else:
    print("del f.__code__ should have raised TypeError")

# Issue #18093: __code__ attribute of a function should be read-only
def f():
    pass

try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ = None should have raised TypeError")

# Issue #18093: __code__ attribute of a function should be read-only
def f():
    pass

try:
    del f.__code__
except TypeError:
