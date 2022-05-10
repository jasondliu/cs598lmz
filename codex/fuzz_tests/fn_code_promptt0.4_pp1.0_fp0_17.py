fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('a',)
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2)
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a',)
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = '\x01\x01'
# Test fn.__code__.co_name
fn.__code__.co_name = 'test'
# Test fn
