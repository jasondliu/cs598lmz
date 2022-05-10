fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = None
try:
    f()
except TypeError:
    pass

# Issue #23897: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = 1
try:
    f()
except TypeError:
    pass

# Issue #23897: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = "a"
try:
    f()
except TypeError:
    pass

# Issue #23897: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = b"a"
try:
    f()
except TypeError:
    pass

# Issue #23897: segfault when calling a function
