fn = lambda: None
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b''
# Test fn.__code__.co_consts
fn.__code__.co_consts = ()
# Test fn.__code__.co_names
fn.__code__.co_names = ()
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ()
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ()
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ()

# Test fn.__code__.co_stacksize
@types.coroutine
def coro():
    yield
fn.__code__.co_stacksize = 1
try:
    fn.__code__.co_stacksize = -1
except ValueError:
    pass

# Test fn.
