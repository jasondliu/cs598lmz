fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #18077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 42
f()

# Issue #18077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = "not a code object"
f()

# Issue #18077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = b"not a code object"
f()

# Issue #18077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = bytearray(b"not a code object")
f()

# Issue #18077: segfault when __code__ is not a code object
def f():
   
