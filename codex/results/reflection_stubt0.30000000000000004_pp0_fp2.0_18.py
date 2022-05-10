fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 'not a code object'
fn()

# __code__.co_argcount is not an integer
fn = lambda: None
fn.__code__.co_argcount = 'not an integer'
fn()

# __code__.co_argcount is negative
fn = lambda: None
fn.__code__.co_argcount = -1
fn()

# __code__.co_argcount is greater than 255
fn = lambda: None
fn.__code__.co_argcount = 256
fn()

# __code__.co_nlocals is not an integer
fn = lambda: None
fn.__code__.co_nlocals = 'not an integer'
fn()

# __code__.co_nlocals is negative
fn = lambda: None
fn.__code__.co_nlocals = -1
fn()

# __code__.co_nlocals is greater than 255
fn = lambda: None
