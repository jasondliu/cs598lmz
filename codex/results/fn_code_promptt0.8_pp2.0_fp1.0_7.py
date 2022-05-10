fn = lambda: None
# Test fn.__code__.co_name
fn.__code__.co_name = 'x'

# Test fn.__code__.co_filename
fn.__code__.co_filename = 'x'

# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 100
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'x' * 1000

# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ['x'] * 10000

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ['x'] * 10000

# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 100

# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
def fn(): pass
fn.__code__.co_flags = CO_VARARGS
def fn(): pass

