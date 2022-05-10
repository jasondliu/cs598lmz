fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute of a builtin function cannot be set.
def f():
    pass
f.__code__ = 1

# Test that the __code__ attribute of a builtin method cannot be set.
def f():
    pass
f.__code__ = 1

# Test that the __code__ attribute of a function cannot be set to a non-code object.
def f():
    pass
f.__code__ = 1

# Test that the __code__ attribute of a function cannot be set to a code object with a different number of arguments.
def f():
    pass
f.__code__ = (lambda: None).__code__

# Test that the __code__ attribute of a function cannot be set to a code object with a different number of locals.
def f():
    pass
f.__code__ = (lambda: None).__code__

# Test that the __code__ attribute of a function cannot be set to a code object with a different number of cells.
def f():
    pass
f.__code__ = (lambda: None).
