fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23
def f():
    yield
    return

# Issue #24
def f():
    yield
    yield
    return

# Issue #25
def f():
    yield
    yield
    yield
    return

# Issue #26
def f():
    yield
    yield
    yield
    yield
    return

# Issue #27
def f():
    yield
    yield
    yield
    yield
    yield
    return

# Issue #28
def f():
    yield
    yield
    yield
    yield
    yield
    yield
    return

# Issue #29
def f():
    yield
    yield
    yield
    yield
    yield
    yield
    yield
    return

# Issue #30
def f():
    yield
    yield
    yield
    yield
    yield
    yield
    yield
    yield
    return

# Issue #31
def f():
    yield
    yield
    yield
    yield
    yield
    yield
    yield
    yield
    yield

