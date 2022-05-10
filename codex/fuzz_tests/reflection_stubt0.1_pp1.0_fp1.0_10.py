fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: test that the __code__ attribute of a built-in function
# cannot be set to a non-code object.
def f():
    pass

try:
    f.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("setting __code__ to a non-code object should fail")

# Issue #23897: test that the __code__ attribute of a built-in function
# cannot be deleted.
def f():
    pass

try:
    del f.__code__
except TypeError:
    pass
else:
    raise Exception("deleting __code__ should fail")

# Issue #23897: test that the __code__ attribute of a built-in function
# cannot be set to a code object with a different number of arguments.
def f():
    pass

try:
    f.__code__ = type(f)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
except TypeError:
    pass
else:
