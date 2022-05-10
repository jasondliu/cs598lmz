fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #20897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #20897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = 'not a code object'
f()

# Issue #20897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = object()
f()

# Issue #20897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = type
f()

# Issue #20897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = type(f.__code__)
f()

# Issue #20897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = type(f.__code__)(f.__code__)
f()


