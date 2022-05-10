fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17095: test that the __code__ attribute of a function is read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ is not read-only")

# Issue #17095: test that the __code__ attribute of a function is read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print("f.__code__ is not read-only")

# Issue #17095: test that the __code__ attribute of a function is read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ is not read-only")

# Issue #17095: test that the __code__ attribute of a function is read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print
