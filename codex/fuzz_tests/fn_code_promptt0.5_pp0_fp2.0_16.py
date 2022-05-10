fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', code)

# Test fn.__code__.co_argcount
setattr(code, 'co_argcount', 0)

# Test fn.__code__.co_consts
setattr(code, 'co_consts', (None, 1, 2, 3))

# Test fn.__code__.co_nlocals
setattr(code, 'co_nlocals', 0)

# Test fn.__code__.co_varnames
setattr(code, 'co_varnames', ())

# Test fn.__defaults__
setattr(fn, '__defaults__', (1, 2, 3))

# Test fn.__globals__
setattr(fn, '__globals__', {})

# Test fn.__kwdefaults__
setattr(fn, '__kwdefaults__', {'a': 1, 'b': 2, 'c': 3})

# Test fn.__name__
setattr(fn, '__name__', 'fn')


