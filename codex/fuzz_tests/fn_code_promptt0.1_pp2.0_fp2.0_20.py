fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 3
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_consts
fn.__code__.co_consts = (None, 'a', 'b', 'c')
# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b', 'c')
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 3
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 2
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_l
