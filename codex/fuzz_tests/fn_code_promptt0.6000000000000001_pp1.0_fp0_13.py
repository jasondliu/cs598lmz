fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 3
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 4
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 5
# Test fn.__code__.co_flags
fn.__code__.co_flags = 6
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 7
# Test fn.__code__.co_code
fn.__code__.co_code = b'code'
# Test fn.__code__.co_consts
fn.__code__.co_consts = 'consts'
# Test fn.__code__.co_names
fn.__code__.co_names = 'names'
# Test fn.__code__.co_
