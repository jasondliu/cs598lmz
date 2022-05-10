fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18072: crash when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #18072: crash when __code__ is not a code object
def f():
    pass
f.__code__ = "not a code object"
f()

# Issue #18072: crash when __code__ is not a code object
def f():
    pass
f.__code__ = 42
f()

# Issue #18072: crash when __code__ is not a code object
def f():
    pass
f.__code__ = object()
f()

# Issue #18072: crash when __code__ is not a code object
def f():
    pass
f.__code__ = type
f()

# Issue #18072: crash when __code__ is not a code object
def f():
    pass
f.__code__ = f
f()

# Issue #18072: crash when __code__ is not a code object
def f
