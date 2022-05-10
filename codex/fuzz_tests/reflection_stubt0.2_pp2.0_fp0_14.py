fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27095: __code__ must be a code object
def fn(): pass
fn.__code__ = None
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #27095: __code__ must be a code object
def fn(): pass
fn.__code__ = "not a code object"
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #27095: __code__ must be a code object
def fn(): pass
fn.__code__ = 1
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #27095: __code__ must be a code object
def fn(): pass
fn.__code__ = 1.0
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #2709
