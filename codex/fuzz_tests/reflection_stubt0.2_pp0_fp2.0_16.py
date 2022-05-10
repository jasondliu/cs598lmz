fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified in place.
def f():
    pass

f.__code__ = (i for i in ())

# Test that the code object is not modified in place.
def f():
    pass

f.__code__ = (i for i in ())

# Test that the code object is not modified in place.
def f():
    pass

f.__code__ = (i for i in ())

# Test that the code object is not modified in place.
def f():
    pass

f.__code__ = (i for i in ())

# Test that the code object is not modified in place.
def f():
    pass

f.__code__ = (i for i in ())

# Test that the code object is not modified in place.
def f():
    pass

f.__code__ = (i for i in ())

# Test that the code object is not modified in place.
def f():
    pass

f.__code__ = (i for i in ())

# Test that
