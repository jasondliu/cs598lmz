fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', _code((
    ('co_argcount', 1),
    ('co_varnames', ('a', 'b', 'c',)),
)))
print(fn.__code__.co_varnames)
# Test fn.__code__.co_flags
setattr(fn, '__code__', _code((
    ('co_flags', 0x00000008),
)))
print(fn.__code__.co_flags)
# Test fn.__code__.co_argcount
setattr(fn, '__code__', _code((
    ('co_argcount', 3),
)))
print(fn.__code__.co_argcount)
# Test fn.__code__.co_posonlyargcount
setattr(fn, '__code__', _code((
    ('co_posonlyargcount', 3),
)))
print(fn.__code__.co_posonlyargcount)

# Test fn.__code__.co_argcount
# Test fn.__code__.co
