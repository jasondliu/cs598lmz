fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: __code__ must be a code object
def fn():
    pass
fn.__code__ = None
fn()

# Issue #23897: __code__ must be a code object
def fn():
    pass
fn.__code__ = 'not a code object'
fn()

# Issue #23897: __code__ must be a code object
def fn():
    pass
fn.__code__ = 1
fn()

# Issue #23897: __code__ must be a code object
def fn():
    pass
fn.__code__ = object()
fn()

# Issue #23897: __code__ must be a code object
def fn():
    pass
fn.__code__ = type
fn()

# Issue #23897: __code__ must be a code object
def fn():
    pass
fn.__code__ = fn
fn()

# Issue #23897: __code__ must be a code object
def fn():
    pass
fn.__code__ = fn.__
