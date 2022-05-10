fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: crash when __code__ is a generator
def f():
    yield 1
f.__code__ = f()
f()

# Issue #24094: crash when __code__ is a generator
def f():
    yield 1
f.__code__ = f()
f()

# Issue #24094: crash when __code__ is a generator
def f():
    yield 1
f.__code__ = f()
f()

# Issue #24094: crash when __code__ is a generator
def f():
    yield 1
f.__code__ = f()
f()

# Issue #24094: crash when __code__ is a generator
def f():
    yield 1
f.__code__ = f()
f()

# Issue #24094: crash when __code__ is a generator
def f():
    yield 1
f.__code__ = f()
f()

# Issue #24094: crash when __code__ is a generator
def f():
    yield 1
f.
