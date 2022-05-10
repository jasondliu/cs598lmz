fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 6

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1, 2)

# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2)

# Test fn.__code__.co_filename
fn.__code__.co_filename = 'foo.py'

# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1

# Test fn.__code__.co_flags
fn.__code__.co_flags = 0

# Test fn.__code__.co_freevars
fn.__code__.co_freevars = (1, 2)

# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 1

# Test fn.__code__.co_lnotab
fn.__code__.co_lnot
