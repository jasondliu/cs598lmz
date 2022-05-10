fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: Crash when __code__ is not a code object.
def f():
    pass
f.__code__ = None
f()

# Issue #23897: Crash when __code__ is not a code object.
def f():
    pass
f.__code__ = 42
f()

# Issue #23897: Crash when __code__ is not a code object.
def f():
    pass
f.__code__ = "foo"
f()

# Issue #23897: Crash when __code__ is not a code object.
def f():
    pass
f.__code__ = object()
f()

# Issue #23897: Crash when __code__ is not a code object.
def f():
    pass
f.__code__ = lambda: None
f()

# Issue #23897: Crash when __code__ is not a code object.
def f():
    pass
f.__code__ = (i for i in ())
f()

# Issue #23897: Crash when __
