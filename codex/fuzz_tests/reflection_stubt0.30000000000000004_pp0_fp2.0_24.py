fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #19092: Ensure that the __code__ attribute of a function is
# not reset to None when the function is garbage collected.
def f():
    pass
def g():
    f.__code__ = None
weakref.finalize(f, g)
del f
gc.collect()

# Issue #19092: Ensure that the __code__ attribute of a function is
# not reset to None when the function is garbage collected.
def f():
    pass
def g():
    f.__code__ = None
weakref.finalize(f, g)
del f
gc.collect()

# Issue #19092: Ensure that the __code__ attribute of a function is
# not reset to None when the function is garbage collected.
def f():
    pass
def g():
    f.__code__ = None
weakref.finalize(f, g)
del f
gc.collect()

# Issue #19092: Ensure that the __code__ attribute of a function is
# not reset to None when the function is garbage collected.

