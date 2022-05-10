fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = type('code', (), {'co_varnames': ('a', 'b', 'c')})
assert fn.__code__.co_varnames == ('a', 'b', 'c')

# Test fn.__code__.co_argcount
fn.__code__ = type('code', (), {'co_argcount': 42})
assert fn.__code__.co_argcount == 42

# Test fn.__code__.co_consts
fn.__code__ = type('code', (), {'co_consts': (1, 2, 3)})
assert fn.__code__.co_consts == (1, 2, 3)

# Test fn.__code__.co_cellvars
fn.__code__ = type('code', (), {'co_cellvars': ('a', 'b', 'c')})
assert fn.__code__.co_cellvars == ('a', 'b', 'c')

# Test fn.__code__.co_freevars
fn.
