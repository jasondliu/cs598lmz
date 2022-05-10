fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2)
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = '\x01\x02'
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('a',)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a',
