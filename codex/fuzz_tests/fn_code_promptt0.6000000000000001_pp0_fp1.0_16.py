fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'co_filename'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 2
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('freevars',)
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = 'co_lnotab'
# Test fn.__code__.co_name
fn.__code__.co_name = 'co_name'
# Test fn.__code__.co_names
fn.__code__.co_names = ('names',)
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 3
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 4
# Test fn.
