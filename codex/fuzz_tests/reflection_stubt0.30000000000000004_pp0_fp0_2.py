fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18897: segfault when __code__ is not a code object
def f(): pass
f.__code__ = 42
try:
    f()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #18897: segfault when __code__ is not a code object
def f(): pass
f.__code__ = None
try:
    f()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #18897: segfault when __code__ is not a code object
def f(): pass
f.__code__ = "foo"
try:
    f()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #18897: segfault when __code__ is not a code object
def f(): pass
f.__code__ = b"foo"
try:
    f()
except TypeError:
    pass
else:
