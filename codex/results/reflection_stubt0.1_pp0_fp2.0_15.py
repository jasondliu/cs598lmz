fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #18071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f.__code__.co_filename

# Issue #18071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f.__code__.co_name

# Issue #18071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f.__code__.co_firstlineno

# Issue #18071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f.__code__.co_flags

# Issue #18071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f.__code__.
