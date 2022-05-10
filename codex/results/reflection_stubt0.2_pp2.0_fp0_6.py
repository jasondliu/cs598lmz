fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #11897: test that the __code__ attribute of a function is
# writable.
def f():
    pass
f.__code__ = f.__code__

# Issue #11897: test that the __code__ attribute of a function is
# writable.
def f():
    pass
f.__code__ = f.__code__

# Issue #11897: test that the __code__ attribute of a function is
# writable.
def f():
    pass
f.__code__ = f.__code__

# Issue #11897: test that the __code__ attribute of a function is
# writable.
def f():
    pass
f.__code__ = f.__code__

# Issue #11897: test that the __code__ attribute of a function is
# writable.
def f():
    pass
f.__code__ = f.__code__

# Issue #11897: test that the __code__ attribute of a function is
# writable.
def f():

