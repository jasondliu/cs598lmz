fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('a', 'b', 'c')
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test.py'
# Test fn.__code__.co_name
fn.__code__.co_name = 'test'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = '\x00\x
