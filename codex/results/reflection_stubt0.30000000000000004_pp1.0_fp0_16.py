fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #25603: test that the __code__ attribute of a function is not
# writable when the function was created by a built-in function.
def f():
    pass
f.__code__ = None

# Issue #25603: test that the __code__ attribute of a function is not
# writable when the function was created by a built-in function.
def f():
    pass
f.__code__ = None

# Issue #25603: test that the __code__ attribute of a function is not
# writable when the function was created by a built-in function.
def f():
    pass
f.__code__ = None

# Issue #25603: test that the __code__ attribute of a function is not
# writable when the function was created by a built-in function.
def f():
    pass
f.__code__ = None

# Issue #25603: test that the __code__ attribute of a function is not
# writable when the function was created by a built-in function.
def f():
    pass
f.
