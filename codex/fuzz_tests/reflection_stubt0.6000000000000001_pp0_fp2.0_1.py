fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi
fn()

# issue29091: crash on free of uninitialized code object
def f():
    raise Exception
f.__code__ = None
try:
    f()
except Exception:
    pass

# issue29091: crash on free of uninitialized code object
def f():
    raise Exception
f.__code__ = None
f.__defaults__ = ()
try:
    f()
except Exception:
    pass

# issue29091: crash on free of uninitialized code object
def f():
    raise Exception
f.__code__ = None
f.__defaults__ = (1,)
try:
    f()
except Exception:
    pass

# issue29091: crash on free of uninitialized code object
def f():
    raise Exception
f.__code__ = None
f.__kwdefaults__ = {}
try:
    f()
except Exception:
    pass

# issue29091: crash on free of uninitialized code object
def f():
    raise Exception
f.__code__ = None
