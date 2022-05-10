fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: test that the __code__ attribute of a built-in function
# is not writable.
def f(): pass
f.__code__ = None

# Issue #23897: test that the __code__ attribute of a built-in method
# is not writable.
def f(): pass
f.__code__ = None

# Issue #23897: test that the __code__ attribute of a built-in method
# is not writable.
def f(): pass
f.__code__ = None

# Issue #23897: test that the __code__ attribute of a built-in method
# is not writable.
def f(): pass
f.__code__ = None

# Issue #23897: test that the __code__ attribute of a built-in method
# is not writable.
def f(): pass
f.__code__ = None

# Issue #23897: test that the __code__ attribute of a built-in method
# is not writable.
def f(): pass
f.__code__
