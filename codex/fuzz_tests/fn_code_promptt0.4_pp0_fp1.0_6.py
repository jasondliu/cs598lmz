fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'bar'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 42
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = '\x00'
# Test fn.__code__.co_name
fn.__code__.co_name = 'foo'
# Test fn.__code__.co_names
fn.__code__.co_names = ()
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 0
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 0
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ()
# Test fn.__code__.co_consts
fn.__code__
