fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 3
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2, 3)
# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b', 'c')
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = '\x01\x01\x01\x01'
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a', 'b', 'c')
# Test fn
