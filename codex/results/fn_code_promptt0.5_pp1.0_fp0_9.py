fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = type('code', (), {'co_varnames': 'a b c'.split()})
assert fn.__code__.co_varnames == ('a', 'b', 'c')

# Test fn.__code__.co_argcount
fn.__code__ = type('code', (), {'co_argcount': 3})
assert fn.__code__.co_argcount == 3

# Test fn.__code__.co_flags
fn.__code__ = type('code', (), {'co_flags': 0})
assert fn.__code__.co_flags == 0

# Test fn.__code__.co_consts
fn.__code__ = type('code', (), {'co_consts': (1, 2, 3)})
assert fn.__code__.co_consts == (1, 2, 3)

# Test fn.__code__.co_code
fn.__code__ = type('code', (), {'co_code': b'1234'})
assert fn.__
