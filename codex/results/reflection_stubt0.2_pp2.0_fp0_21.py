fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27071: crash when __code__ is set to a non-code object
def f():
    pass
def g():
    pass
f.__code__ = g
f()

# Issue #27071: crash when __code__ is set to a non-code object
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f()

# Issue #27071: crash when __code__ is set to a non-code object
def f():
    pass
def g():
    pass
f.__code__ = g.__code__.__code__
f()

# Issue #27071: crash when __code__ is set to a non-code object
def f():
    pass
def g():
    pass
f.__code__ = g.__code__.__code__.__code__
f()

# Issue #27071: crash when __code__ is set to a non-code object
def f():
    pass
def g():
    pass
f
