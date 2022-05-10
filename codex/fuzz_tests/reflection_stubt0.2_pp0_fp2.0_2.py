fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #12077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #12077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = "foo"
f()

# Issue #12077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = {}
f()

# Issue #12077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = []
f()

# Issue #12077: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = ()
f()

# Issue #12077
