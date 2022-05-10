fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not a code object
def fn():
    pass
fn.__code__ = 1
fn()

# __code__ is a class
def fn():
    pass
fn.__code__ = type
fn()

# __code__ is an instance of a class
def fn():
    pass
fn.__code__ = type()
fn()

# __code__ is a code object with an invalid argcount
def fn():
    pass
fn.__code__ = type(fn).__code__._replace(co_argcount=-1)
fn()

# __code__ is a code object with an invalid kwonlyargcount
def fn():
    pass
fn.__code__ = type(fn).__code__._replace(co_kwonlyargcount=-1)
fn()

# __code__ is a code object with an invalid flags
def fn():
    pass
fn.__code__ = type(fn).__code__._replace(co_flags=-1)
fn()

# __code__ is a code object with an invalid
