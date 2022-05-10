fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = (1, 2, 3)

# Test fn.__code__.co_consts
# Test fn.__code__.co_consts[0]
# Test fn.__code__.co_consts[0].__code__.co_varnames
fn.__code__.co_consts[0].__code__.co_varnames = (1, 2, 3)
# Test fn.__code__.co_consts[0].__code__.co_argcount
fn.__code__.co_consts[0].__code__.co_argcount = (1, 2, 3)

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1, 2, 3)

# Test fn.__code__.co_freevars
fn.__code__.
