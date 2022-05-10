fn = lambda: None
# Test fn.__code__.co_argcount
setattr(fn, '__code__', types.CodeType(0, 0, 0, 0, 0, '', (), (), (), '', '', 0, b''))

# Test fn.__code__.co_varnames
setattr(fn, '__code__', types.CodeType(0, 0, 0, 0, 0, '', ('x', 'y'), (), (), '', '', 0, b''))

# Test fn.__code__.co_consts
setattr(fn, '__code__', types.CodeType(0, 0, 0, 0, 0, '', (), False, (), '', '', 0, b''))

# Test fn.__code__.co_names
setattr(fn, '__code__', types.CodeType(0, 0, 0, 0, 0, '', (), (), ('x', 'y'), '', '', 0, b''))

# Test fn.__code__.co_varnames and fn.__code__.co_consts
def varnames_consts(x, y
