fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'\x00\x01'
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 2
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b')
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('c', 'd')
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('e', 'f')
# Test fn.__code__.co_consts
fn.__code__.
