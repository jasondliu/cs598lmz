fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27082: crash when a generator is used as a code object
def fn():
    yield
fn.__code__ = fn.__code__
fn()

# Issue #27082: crash when a generator is used as a code object
def fn():
    yield
fn.__code__ = fn.__code__.__code__
fn()

# Issue #27082: crash when a generator is used as a code object
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__
fn()

# Issue #27082: crash when a generator is used as a code object
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__.__code__
fn()

# Issue #27082: crash when a generator is used as a code object
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__.__code__.__code__
fn()

# Issue #
