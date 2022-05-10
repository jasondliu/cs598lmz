fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16077: crash when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #16077: crash when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #16077: crash when __code__ is not a code object
def f():
    pass
f.__code__ = "foo"
f()

# Issue #16077: crash when __code__ is not a code object
def f():
    pass
f.__code__ = object()
f()

# Issue #16077: crash when __code__ is not a code object
def f():
    pass
f.__code__ = type
f()

# Issue #16077: crash when __code__ is not a code object
def f():
    pass
f.__code__ = f
f()

# Issue #16077: crash when __code__ is not a code object
def f():
   
