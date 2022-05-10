fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: crash when __code__ is not a code object
def f():
    pass
f.__code__ = None
try:
    f()
except TypeError:
    pass
else:
    print("f() didn't raise TypeError")

# Issue #24071: crash when __code__ is not a code object
def f():
    pass
f.__code__ = 1
try:
    f()
except TypeError:
    pass
else:
    print("f() didn't raise TypeError")

# Issue #24071: crash when __code__ is not a code object
def f():
    pass
f.__code__ = "abc"
try:
    f()
except TypeError:
    pass
else:
    print("f() didn't raise TypeError")

# Issue #24071: crash when __code__ is not a code object
def f():
    pass
f.__code__ = object()
try:
    f()
except TypeError:
    pass
else:
    print
