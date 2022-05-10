fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = '/home/user/test.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 10
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a', 'b')
# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 0
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'\x01\x02'
# Test fn.__code__.co_name
fn.__code__.co_name = 'fn'
# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b')
# Test fn.__code__.co_nlocals
fn.__code__.co_nloc
