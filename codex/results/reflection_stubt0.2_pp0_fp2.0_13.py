fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator can be used as a code object.
def fn():
    yield 1
fn.__code__ = fn()
fn()

# Test that a generator can be used as a code object.
def fn():
    yield 1
fn.__code__ = fn()
fn()

# Test that a generator can be used as a code object.
def fn():
    yield 1
fn.__code__ = fn()
fn()

# Test that a generator can be used as a code object.
def fn():
    yield 1
fn.__code__ = fn()
fn()

# Test that a generator can be used as a code object.
def fn():
    yield 1
fn.__code__ = fn()
fn()

# Test that a generator can be used as a code object.
def fn():
    yield 1
fn.__code__ = fn()
fn()

# Test that a generator can be used as a code object.
def fn():
    yield 1
fn.__code__ = fn()
fn()

# Test that
