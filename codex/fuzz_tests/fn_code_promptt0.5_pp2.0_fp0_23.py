fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', code_object)
fn.__code__.co_varnames

# Test fn.__closure__
setattr(fn, '__closure__', (1, 2, 3))
fn.__closure__

# Test fn.__globals__
setattr(fn, '__globals__', {'a': 1, 'b': 2})
fn.__globals__

# Test fn.__code__.co_consts
setattr(fn, '__code__', code_object)
fn.__code__.co_consts

# Test fn.__call__
setattr(fn, '__call__', lambda: None)
fn.__call__()

# Test fn.__code__.co_filename
setattr(fn, '__code__', code_object)
fn.__code__.co_filename

# Test fn.__code__.co_firstlineno
setattr(fn, '__code__', code_object)
fn.__code__.
