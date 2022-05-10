fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16058: test that the __code__ attribute of a built-in function
# is read-only.
def f(): pass
f.__code__ = 42

# Issue #16058: test that the __code__ attribute of a built-in method
# is read-only.
def f(): pass
f.__code__ = 42

# Issue #16058: test that the __code__ attribute of a built-in method
# is read-only.
def f(): pass
f.__code__ = 42

# Issue #16058: test that the __code__ attribute of a built-in method
# is read-only.
def f(): pass
f.__code__ = 42

# Issue #16058: test that the __code__ attribute of a built-in method
# is read-only.
def f(): pass
f.__code__ = 42

# Issue #16058: test that the __code__ attribute of a built-in method
# is read-only.
def f(): pass
f.__code__
