fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = argcount_code
assert fn.__code__.co_argcount == 0
# Test fn.__code__.co_varnames
fn.__code__ = varnames_code
assert fn.__code__.co_varnames == ('a', 'b')
# Test fn.__code__.co_cellvars
fn.__code__ = cellvars_code
assert fn.__code__.co_cellvars == ('a', 'b')
# Test fn.__code__.co_freevars
fn.__code__ = freevars_code
assert fn.__code__.co_freevars == ('a', 'b')
# Test fn.__code__.co_consts
fn.__code__ = consts_code
assert fn.__code__.co_consts == (None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# Test fn.__code__.co_names
fn.__code__ = names_code
assert fn.
