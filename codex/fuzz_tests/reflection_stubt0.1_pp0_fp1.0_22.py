fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: __code__ setter should not accept a non-code object
def fn():
    pass

try:
    fn.__code__ = fn
except TypeError:
    pass
else:
    raise Exception("__code__ setter should not accept a non-code object")

# Issue #23897: __code__ setter should not accept a non-code object
def fn():
    pass

try:
    fn.__code__ = fn.__code__
except TypeError:
    pass
else:
    raise Exception("__code__ setter should not accept a non-code object")

# Issue #23897: __code__ setter should not accept a non-code object
def fn():
    pass

try:
    fn.__code__ = fn.__code__.__code__
except TypeError:
    pass
else:
    raise Exception("__code__ setter should not accept a non-code object")

# Issue #23897: __code__ setter should not accept a non-code object
