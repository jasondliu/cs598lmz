fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test that __code__ is a readonly attribute
def fn(): pass
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

# test that __code__ is a readonly attribute
def fn(): pass
try:
    del fn.__code__
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

# test that __code__ can be None
def fn(): pass
fn.__code__ = None

# test that __code__ can be set to a code object
def fn(): pass
fn.__code__ = fn.__code__

# test that __code__ can be set to a code object
def fn(): pass
fn.__code__ = fn.__code__

# test that __code__ can be set to a code object
def fn(): pass
fn.__code__ = fn.__code__

# test that __code__ can be set to a code object
def fn(): pass
fn.__code__ =
