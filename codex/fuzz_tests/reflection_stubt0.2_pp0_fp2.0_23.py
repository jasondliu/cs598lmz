fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24984: __code__ attribute of a function should be read-only
def fn():
    pass
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a function should be read-only")

# Issue #24984: __code__ attribute of a function should be read-only
def fn():
    pass
try:
    del fn.__code__
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a function should be read-only")

# Issue #24984: __code__ attribute of a function should be read-only
def fn():
    pass
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a function should be read-only")

# Issue #24984: __code__ attribute of a function should be read-only
def fn():
    pass
try:
    del fn.__code__
except TypeError:
