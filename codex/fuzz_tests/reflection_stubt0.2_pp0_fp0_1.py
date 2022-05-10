fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18071: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #18071: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 42
f()

# Issue #18071: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = "hello"
f()

# Issue #18071: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = {}
f()

# Issue #18071: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = []
f()

# Issue #18071: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = ()
f()

# Issue #18071
