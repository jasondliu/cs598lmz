from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we don't crash on a function with a __code__ that is not a
# PyCodeObject.
def f():
    pass
f.__code__ = None
list(f)

# Test that we don't crash on a function with a __code__ that is not a
# PyCodeObject.
def f():
    pass
f.__code__ = None
list(f)

# Test that we don't crash on a function with a __code__ that is not a
# PyCodeObject.
def f():
    pass
f.__code__ = None
list(f)

# Test that we don't crash on a function with a __code__ that is not a
# PyCodeObject.
def f():
    pass
f.__code__ = None
list(f)

# Test that we don't crash on a function with a __code__ that is not a
# PyCodeObject.
def f():
    pass
f.__code__ = None
list(f)

# Test that we don't crash
