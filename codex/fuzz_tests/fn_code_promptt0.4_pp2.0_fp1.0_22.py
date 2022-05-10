fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = "test"
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ()
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b"\x00\x00"
# Test fn.__code__.co_name
fn.__code__.co_name = "test"
# Test fn.__code__.co_names
fn.__code__.co_names = ()
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 1
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1
# Test fn.__code__.co_varnames

