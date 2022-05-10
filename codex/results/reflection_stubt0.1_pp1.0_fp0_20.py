fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: test that the __code__ attribute of a function is
# read-only.
def f():
    pass

try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a function is not read-only")

# Issue #24071: test that the __code__ attribute of a built-in function
# is read-only.
try:
    len.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in function is not read-only")

# Issue #24071: test that the __code__ attribute of a built-in method
# is read-only.
try:
    [].append.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in method is not read-only")

# Issue #24071: test that the __code__ attribute of a method is
# read-only.

