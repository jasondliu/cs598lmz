fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1, 2)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = (1, 2)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1, 2)
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2)
# Test fn.__code__.co_names
fn.__code__.co_names = (1, 2)
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'hello world'
# Test fn.__code__.__weakref__
fn.__code__.__weakref__ = 'hello world'

# Test fn.__code__.co_argcount
fn
