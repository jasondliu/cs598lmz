fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a', 'b')
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = '\x00\x01'
# Test fn.__code__.co_name
fn.__code__.co_name = 'fn'
# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b')
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 2
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 2
# Test fn.__
