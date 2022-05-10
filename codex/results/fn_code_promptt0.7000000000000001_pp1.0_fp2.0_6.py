fn = lambda: None
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ['a', 'b']
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b', 'c')
# Test fn.__code__.co_argcount
# TODO: should be 2, not 3
fn.__code__.co_argcount = 3
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('a', 'b')
# Test fn.__code__.co_consts
fn.__code__.co_consts = ('a', 'b')
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'a.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.
