fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('a', 'b')
# Test fn.__code__.co_code
fn.__code__.co_code = b'\x01\x02\x03\x04'
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2, 3)
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a', 'b')
# Test fn.__code__.co_kwonlyargcount
fn.__code__
