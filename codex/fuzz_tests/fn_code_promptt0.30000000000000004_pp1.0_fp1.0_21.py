fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), ('a', 'b'), (), '', '', 0, b'')

# Test fn.__code__.co_cellvars
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), ('a', 'b'), '', '', 0, b'')

# Test fn.__code__.co_freevars
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'a\x00b\x00')

# Test fn.__code__.co_cellvars and fn.__code__.co_freevars
fn.__code__ = types.CodeType(0, 0, 0, 0,
