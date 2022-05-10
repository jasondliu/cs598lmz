fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'foo.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = '1'
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'foo'
# Test fn.__code__.co_name
fn.__code__.co_name = 'foo'
# Test fn.__code__.co_names
fn.__code__.co_names = ('foo', 'bar')
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 'foo'
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 'foo'
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('foo', 'bar')
# Test fn.__code__.co_freevars
fn.__code__.co_freevars
