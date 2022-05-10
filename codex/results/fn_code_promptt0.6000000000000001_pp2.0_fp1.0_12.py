fn = lambda: None
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, b'a', 1.1, fn)

# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (b'a', b'b', b'c')

# Test fn.__code__.co_names
fn.__code__.co_names = (b'abs', b'a')

# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1

# Test fn.__code__.co_flags
fn.__code__.co_flags = 1

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (b'a', b'b')

# Test fn.__code__.co_freevars
fn.__code__.co_freevars = (b'a', b'b')

# Test fn.__code__.co_lnotab
fn.__code__.co
