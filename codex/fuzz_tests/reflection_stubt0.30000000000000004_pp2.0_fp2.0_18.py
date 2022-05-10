fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #15: Crash when calling a function with a bad __code__.
def f():
    pass
f.__code__ = None
try:
    f()
except TypeError:
    pass

# Issue #16: Crash when calling a function with a bad __code__.
def f():
    pass
f.__code__ = ""
try:
    f()
except TypeError:
    pass

# Issue #17: Crash when calling a function with a bad __code__.
def f():
    pass
f.__code__ = 1
try:
    f()
except TypeError:
    pass

# Issue #18: Crash when calling a function with a bad __code__.
def f():
    pass
f.__code__ = {}
try:
    f()
except TypeError:
    pass

# Issue #19: Crash when calling a function with a bad __code__.
def f():
    pass
f.__code__ = []
try:
    f()
except TypeError:
    pass

# Issue #
