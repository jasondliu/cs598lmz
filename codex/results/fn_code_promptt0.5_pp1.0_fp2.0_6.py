fn = lambda: None
# Test fn.__code__.co_flags
setattr(fn.__code__, 'co_flags', 0)
# Test fn.__code__.co_code
setattr(fn.__code__, 'co_code', b'')
# Test fn.__code__.co_consts
setattr(fn.__code__, 'co_consts', ())
# Test fn.__code__.co_names
setattr(fn.__code__, 'co_names', ())
# Test fn.__code__.co_varnames
setattr(fn.__code__, 'co_varnames', ())
# Test fn.__code__.co_freevars
setattr(fn.__code__, 'co_freevars', ())
# Test fn.__code__.co_cellvars
setattr(fn.__code__, 'co_cellvars', ())
# Test fn.__code__.co_filename
setattr(fn.__code__, 'co_filename', '')
# Test fn.__code__.co_name
setattr(fn.__code__
