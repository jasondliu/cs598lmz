fn = lambda: None
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b''
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 0
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2, 3)
# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b', 'c')
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a', 'b', 'c')
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('a', 'b', 'c')
# Test fn.__code__.co
