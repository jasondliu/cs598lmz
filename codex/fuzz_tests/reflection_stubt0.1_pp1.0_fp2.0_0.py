fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: test that the __code__ attribute of a built-in function
# cannot be set to a non-code object.
def f():
    pass

try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #23897: test that the __code__ attribute of a built-in function
# cannot be set to a code object with a different number of arguments.
def f():
    pass

try:
    f.__code__ = (lambda x: None).__code__
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #23897: test that the __code__ attribute of a built-in function
# cannot be set to a code object with a different number of arguments.
def f(x, y):
    pass

try:
    f.__code__ = (lambda x: None).__code__
except TypeError:
    pass
else:
    raise Exception("
