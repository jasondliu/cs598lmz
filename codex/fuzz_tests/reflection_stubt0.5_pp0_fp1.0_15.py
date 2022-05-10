fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17281: crash when __code__ is set to a non-code object
def foo():
    pass

def foo2():
    raise AttributeError

foo.__code__ = foo2
try:
    foo()
except AttributeError:
    pass

# Issue #17281: crash when __code__ is set to a non-code object
def foo():
    pass

def foo2():
    raise AttributeError

foo.__code__ = foo2
try:
    foo()
except AttributeError:
    pass

# Issue #17281: crash when __code__ is set to a non-code object
def foo():
    pass

def foo2():
    raise AttributeError

foo.__code__ = foo2
try:
    foo()
except AttributeError:
    pass

# Issue #17281: crash when __code__ is set to a non-code object
def foo():
    pass

def foo2():
    raise AttributeError

foo.__code__ = foo2
try
