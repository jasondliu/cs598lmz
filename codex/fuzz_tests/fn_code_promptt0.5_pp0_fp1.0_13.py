fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', ())
# Test fn.__code__.co_firstlineno
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 1, b'', ())
# Test fn.__code__.co_name
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), 'name', '', 0, b'', ())
# Test fn.__code__.co_argcount
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', ())
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', ('a',))
# Test fn.__code__.co_cellvars
