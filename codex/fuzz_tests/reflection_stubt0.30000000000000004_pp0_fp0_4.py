fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that __code__ can be deleted
def fn(): pass
del fn.__code__
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that __code__ can be set to None
def fn(): pass
fn.__code__ = None
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that __code__ can be set to a code object
def fn(): pass
fn.__code__ = fn.__code__
fn()

# Test that __code__ can be set to a code object with a different name
def fn(): pass
fn.__code__ = type(fn)(fn.__code__)
fn()

# Test that __code__ can be set to a code object with a different name
def fn(): pass
fn.__code__ = type(fn)(fn.__code__.co_argcount, fn.__code__.co_kwonlyargcount, fn.__code__
