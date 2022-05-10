fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24097: test that the code object is not modified in place
# when it is not writable.
def f():
    pass
f.__code__ = (i for i in ())
f()

# Issue #24097: test that the code object is not modified in place
# when it is not writable.
def f():
    pass
f.__code__ = (i for i in ())
f()

# Issue #24097: test that the code object is not modified in place
# when it is not writable.
def f():
    pass
f.__code__ = (i for i in ())
f()

# Issue #24097: test that the code object is not modified in place
# when it is not writable.
def f():
    pass
f.__code__ = (i for i in ())
f()

# Issue #24097: test that the code object is not modified in place
# when it is not writable.
def f():
    pass
f.__code__ = (i for i
