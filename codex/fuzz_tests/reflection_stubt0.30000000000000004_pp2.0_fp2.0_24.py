fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #19095: __code__ must be a code object
def fn():
    pass
fn.__code__ = None
fn()

# Issue #19095: __code__ must be a code object
def fn():
    pass
fn.__code__ = 'foo'
fn()

# Issue #19095: __code__ must be a code object
def fn():
    pass
fn.__code__ = 1
fn()

# Issue #19095: __code__ must be a code object
def fn():
    pass
fn.__code__ = object()
fn()

# Issue #19095: __code__ must be a code object
def fn():
    pass
fn.__code__ = type
fn()

# Issue #19095: __code__ must be a code object
def fn():
    pass
fn.__code__ = fn
fn()

# Issue #19095: __code__ must be a code object
def fn():
    pass
fn.__code__ = fn.__code__

