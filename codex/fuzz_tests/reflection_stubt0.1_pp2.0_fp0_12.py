fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16077: segfault when __code__ is set to a non-code object
# with a co_code attribute.
def f():
    pass
f.__code__ = 42
try:
    f()
except TypeError:
    pass
else:
    print("f() didn't raise TypeError")

# Issue #16077: segfault when __code__ is set to a non-code object
# with a co_code attribute.
def f():
    pass
f.__code__ = 42
try:
    f()
except TypeError:
    pass
else:
    print("f() didn't raise TypeError")

# Issue #16077: segfault when __code__ is set to a non-code object
# with a co_code attribute.
def f():
    pass
f.__code__ = 42
try:
    f()
except TypeError:
    pass
else:
    print("f() didn't raise TypeError")

# Issue #16077: segfault
