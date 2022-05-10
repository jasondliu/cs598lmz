fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22852: __code__ of a function must be a code object
def fn():
    pass
fn.__code__ = "not a code object"
try:
    fn()
except TypeError:
    pass
else:
    raise Exception

# Issue #22853: __code__ of a function must be a code object
def fn():
    pass
fn.__code__ = object()
try:
    fn()
except TypeError:
    pass
else:
    raise Exception

# Issue #22854: __code__ of a function must be a code object
def fn():
    pass
fn.__code__ = object()
try:
    fn()
except TypeError:
    pass
else:
    raise Exception

# Issue #22855: __code__ of a function must be a code object
def fn():
    pass
fn.__code__ = None
try:
    fn()
except TypeError:
    pass
else:
    raise Exception

# Issue #22856: __code__ of a function must be a code object
