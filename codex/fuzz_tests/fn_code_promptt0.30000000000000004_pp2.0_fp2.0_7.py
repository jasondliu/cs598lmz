fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'foo'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('foo',)
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = 'foo'
# Test fn.__code__.co_name
fn.__code__.co_name = 'foo'
# Test fn.__code__.co_names
fn.__code__.co_names = ('foo',)
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 1
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1
# Test fn.__code__.co_varnames

