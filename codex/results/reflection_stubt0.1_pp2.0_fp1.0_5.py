fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #24071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #24071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #24071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #24071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #24071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()
f()

# Issue #24071: crash when __code__ is a generator
def f():
    yield
f.__code__ = f()

