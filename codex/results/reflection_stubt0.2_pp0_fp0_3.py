fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27095: __code__ should be read-only
def f(): pass
try:
    f.__code__ = 42
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only")

# Issue #27095: __code__ should be read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only")

# Issue #27095: __code__ should be read-only
def f(): pass
try:
    f.__code__ += 42
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only")

# Issue #27095: __code__ should be read-only
def f(): pass
try:
    f.__code__ -= 42
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only")

# Issue #27095: __code__ should be read
