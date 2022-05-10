fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not a generator.
def fn():
    yield
fn.__code__ = fn.__code__
fn()

# Test that the code object is not a generator.
def fn():
    yield
fn.__code__ = fn.__code__.__code__
fn()

# Test that the code object is not a generator.
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__
fn()

# Test that the code object is not a generator.
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__.__code__
fn()

# Test that the code object is not a generator.
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__.__code__.__code__
fn()

# Test that the code object is not a generator.
def fn():
    yield
fn.__code__ = fn.__code__.__code
