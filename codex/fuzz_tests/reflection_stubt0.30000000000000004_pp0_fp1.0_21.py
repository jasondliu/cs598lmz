fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12079: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #12079: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #12079: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #12079: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #12079: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #12079: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #12079: se
