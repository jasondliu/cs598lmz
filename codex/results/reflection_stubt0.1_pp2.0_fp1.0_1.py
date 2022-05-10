fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #23897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = 1
f()

# Issue #23897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = "abc"
f()

# Issue #23897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = object()
f()

# Issue #23897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = []
f()

# Issue #23897: crash when __code__ is not a code object
def f():
    pass
f.__code__ = {}
f()

# Issue #23897: crash when __code__ is not a code object
def f():
   
