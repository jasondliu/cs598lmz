fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #28429: Crash when __code__ is deleted
def f():
    pass
del f.__code__
try:
    f()
except TypeError:
    pass

# Issue #28429: Crash when __code__ is set to None
def f():
    pass
f.__code__ = None
try:
    f()
except TypeError:
    pass

# Issue #28429: Crash when __code__ is set to a code object
def f():
    pass
f.__code__ = f.__code__
f()

# Issue #28429: Crash when __code__ is set to a code object with a NULL co_code
def f():
    pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
try:
    f()
except ValueError:
    pass

# Issue #28429: Crash when __code__ is set to a code object with a non-NULL co_code
def f():
   
