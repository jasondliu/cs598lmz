fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# code object with non-code attributes
def fn():
    pass
fn.__code__.co_firstlineno = 'a'
fn()
fn.__code__.co_firstlineno = 1.0
fn()
fn.__code__.co_firstlineno = object()
fn()
fn.__code__.co_firstlineno = -1
fn()
fn.__code__.co_firstlineno = 2**32
fn()

# code object with non-code attributes
def fn():
    pass
fn.__code__.co_lnotab = 1
fn()
fn.__code__.co_lnotab = 'a'
fn()
fn.__code__.co_lnotab = object()
fn()
fn.__code__.co_lnotab = -1
fn()
fn.__code__.co_lnotab = 2**32
fn()

# code object with non-code attributes
def fn():
    pass
fn.__code__.co_freevars = 1

