fn = lambda: None
# Test fn.__code__.co_filename
setattr(fn, '__code__', type('code', (), {'co_filename': 'test'}))
assert fn.__code__.co_filename == 'test'

# Test fn.__code__.co_firstlineno
setattr(fn, '__code__', type('code', (), {'co_firstlineno': 1}))
assert fn.__code__.co_firstlineno == 1

# Test fn.__code__.co_name
setattr(fn, '__code__', type('code', (), {'co_name': 'fn'}))
assert fn.__code__.co_name == 'fn'

# Test fn.__code__.co_varnames
setattr(fn, '__code__', type('code', (), {'co_varnames': ('a', 'b')}))
assert fn.__code__.co_varnames == ('a', 'b')

# Test fn.__code__.co_argcount
setattr(fn, '__code__', type('code', (),
