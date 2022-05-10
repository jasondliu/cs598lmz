fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24091: test that the __code__ attribute of a built-in function
# is not writable.
def f():
    pass
def g():
    pass
f.__code__ = g.__code__

# Issue #24091: test that the __code__ attribute of a built-in method
# is not writable.
def f():
    pass
def g():
    pass
f.__code__ = g.__code__

# Issue #24091: test that the __code__ attribute of a built-in method
# is not writable.
def f():
    pass
def g():
    pass
f.__code__ = g.__code__

# Issue #24091: test that the __code__ attribute of a built-in method
# is not writable.
def f():
    pass
def g():
    pass
f.__code__ = g.__code__

# Issue #24091: test that the __code__ attribute of a built-in method
# is not writable.

