fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', type('code', (object,), {'co_varnames': ('a', 'b')}))
print(fn.__code__.co_varnames)

# Test fn.__code__.co_argcount
setattr(fn, '__code__', type('code', (object,), {'co_argcount': 2}))
print(fn.__code__.co_argcount)

# Test fn.__code__.co_flags
setattr(fn, '__code__', type('code', (object,), {'co_flags': 0}))
print(fn.__code__.co_flags)

# Test fn.__code__.co_code
setattr(fn, '__code__', type('code', (object,), {'co_code': '123'}))
print(fn.__code__.co_code)

# Test fn.__code__.co_consts
setattr(fn, '__code__', type('code', (object,
