fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = type('code', (), {'co_varnames': ('a', 'b', 'c')})
x = fn.__code__.co_varnames
# Test fn.__code__.co_argcount
fn.__code__ = type('code', (), {'co_argcount': 3})
x = fn.__code__.co_argcount
# Test fn.__code__.co_flags
fn.__code__ = type('code', (), {'co_flags': 0x08})
x = fn.__code__.co_flags
# Test fn.__code__.co_names
fn.__code__ = type('code', (), {'co_names': ('a', 'b', 'c')})
x = fn.__code__.co_names
# Test fn.__code__.co_consts
fn.__code__ = type('code', (), {'co_consts': (1, 2, 3)})
x = fn.__code__.co_consts
# Test fn.__code
