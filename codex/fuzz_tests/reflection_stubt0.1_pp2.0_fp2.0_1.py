fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: Ensure that the __code__ attribute of a function is
# read-only.
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute should be read-only")

# Issue #23897: Ensure that the __code__ attribute of a function is
# read-only.
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    raise Exception("__code__ attribute should be read-only")

# Issue #23897: Ensure that the __code__ attribute of a function is
# read-only.
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute should be read-only")

# Issue #23897: Ensure that the __code__ attribute of a function is
# read-only.
def f(): pass
try:
    del f.__code__
except
