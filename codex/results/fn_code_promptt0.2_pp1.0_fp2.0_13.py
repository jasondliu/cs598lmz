fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2)
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2)
# Test fn.__code__.co_names
fn.__code__.co_names = (1, 2)
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 1
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1
# Test fn.__code__.co_code
fn.__code__.co_code = b'1'
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'1'
# Test fn.__code__.
