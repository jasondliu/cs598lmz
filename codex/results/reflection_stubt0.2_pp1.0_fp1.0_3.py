fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: Check that __code__ is not set to a non-code object
# when the function is created.
def f():
    pass
f.__code__ = 1

# Issue #23897: Check that __code__ is not set to a non-code object
# when the function is created.
def f():
    pass
f.__code__ = 1

# Issue #23897: Check that __code__ is not set to a non-code object
# when the function is created.
def f():
    pass
f.__code__ = 1

# Issue #23897: Check that __code__ is not set to a non-code object
# when the function is created.
def f():
    pass
f.__code__ = 1

# Issue #23897: Check that __code__ is not set to a non-code object
# when the function is created.
def f():
    pass
f.__code__ = 1

# Issue #23897: Check that __code__ is not set to a non
