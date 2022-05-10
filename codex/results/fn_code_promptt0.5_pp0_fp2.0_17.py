fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 3
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 4
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3, 4)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1, 2, 3, 4)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = (1, 2, 3, 4)
# Test fn.__code__.co_names
fn.__code__.co_names = (1, 2, 3, 4)
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'a'
# Test fn.__code__.co_name
fn.__code__.co_name = 'b'
# Test fn.__code__.co_firstlineno
fn.
