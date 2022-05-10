fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'filename'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = 'lnotab'
# Test fn.__code__.co_name
fn.__code__.co_name = 'name'
# Test fn.__code__.co_names
fn.__code__.co_names = ('names',)
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 1
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('varnames',)

# Test fn.__code__.co
