fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1,)
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = 1
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = (1,)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1,)

# Test fn.__code__.co_filename
fn.__code__.co_filename = 'a'
# Test fn.__code__.co_name
fn.__code__.co_name = 'a'
# Test fn.__code__.co_names
fn
