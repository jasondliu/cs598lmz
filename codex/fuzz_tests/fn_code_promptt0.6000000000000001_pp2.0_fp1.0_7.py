fn = lambda: None
# Test fn.__code__.co_flags.
fn.__code__.co_flags = 0
# Test fn.__code__.co_consts[i].
fn.__code__.co_consts = ()
# Test fn.__code__.co_names[i].
fn.__code__.co_names = ()
# Test fn.__code__.co_varnames[i].
fn.__code__.co_varnames = ()
# Test fn.__code__.co_freevars[i].
fn.__code__.co_freevars = ()
# Test fn.__code__.co_cellvars[i].
fn.__code__.co_cellvars = ()

# Test fn.__code__.co_stacksize.
def fn():
    return 1
fn.__code__.co_stacksize = 2

# Test fn.__code__.co_lnotab.
def fn():
    return 1
fn.__code__.co_lnotab = b'\x00'

# Test fn.__code
