fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18078: test that the code object of a function is not
# modified when the function is called.
def f():
    pass
code = f.__code__
f()
assert code is f.__code__

# Issue #18078: test that the code object of a function is not
# modified when the function is called.
def f():
    pass
code = f.__code__
f()
assert code is f.__code__

# Issue #18078: test that the code object of a function is not
# modified when the function is called.
def f():
    pass
code = f.__code__
f()
assert code is f.__code__

# Issue #18078: test that the code object of a function is not
# modified when the function is called.
def f():
    pass
code = f.__code__
f()
assert code is f.__code__

# Issue #18078: test that the code object of a function is not
# modified when the function is called.
def
