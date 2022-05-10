fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = type('code', (), {'co_varnames': ('a',)})
# Test fn.__code__.co_argcount
fn.__code__ = type('code', (), {'co_argcount': 1})
# Test fn.__code__.co_argcount
fn.__code__ = type('code', (), {'co_argcount': -1})
# Test fn.__code__.co_flags
fn.__code__ = type('code', (), {'co_flags': 0x4})
# Test fn.__code__.co_flags
fn.__code__ = type('code', (), {'co_flags': 0x4000})
# Test fn.__code__.co_flags
fn.__code__ = type('code', (), {'co_flags': 0x400000})
# Test fn.__code__.co_flags
fn.__code__ = type('code', (), {'co_flags': 0x40})
# Test fn.__code__.co_flags
fn.__code__
