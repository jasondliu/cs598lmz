fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called even if it is not
# fully initialized.
def f():
    yield
f.__code__ = (i for i in ())
f()

# Test that a generator function can be called even if it is not
# fully initialized.
def f():
    yield
f.__code__ = (i for i in ())
f()

# Test that a generator function can be called even if it is not
# fully initialized.
def f():
    yield
f.__code__ = (i for i in ())
f()

# Test that a generator function can be called even if it is not
# fully initialized.
def f():
    yield
f.__code__ = (i for i in ())
f()

# Test that a generator function can be called even if it is not
# fully initialized.
def f():
    yield
f.__code__ = (i for i in ())
f()

# Test that a generator function can be called even if it is not
# fully initialized.
def f():
    yield
f
