fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b')
assert fn.__code__.co_varnames == ('a', 'b')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
assert fn.__code__.co_argcount == 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
assert fn.__code__.co_flags == 0

# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2, 3)
assert fn.__code__.co_consts == (1, 2, 3)

# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b')
assert fn.__code__.co_names == ('a', 'b')

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('a', '
