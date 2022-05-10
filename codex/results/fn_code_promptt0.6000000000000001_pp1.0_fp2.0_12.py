fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'a'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_name
fn.__code__.co_name = 'b'
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 0
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ()
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ()
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ()
# Test fn.__code__.co_consts
fn.__code__.co_consts = ()
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_kwonlyargcount
fn.__code__.co
