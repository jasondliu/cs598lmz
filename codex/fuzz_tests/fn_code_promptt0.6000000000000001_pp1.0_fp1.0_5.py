fn = lambda: None
# Test fn.__code__.co_code
fn.__code__.co_code = b'x'
# Test fn.__code__.co_const
fn.__code__.co_consts = (None,)
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'x'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ()
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'x'
# Test fn.__code__.co_name
fn.__code__.co_name = 'x'
# Test fn.__code__.co_names
fn.__code__.co_names = ()
# Test fn.__code__.co_nlocals
fn.__code__.co
