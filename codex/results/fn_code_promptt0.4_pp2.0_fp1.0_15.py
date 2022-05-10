fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 1, b'', ())
fn.__code__.co_varnames = ()
# Test fn.__code__.co_cellvars
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 1, b'', ())
fn.__code__.co_cellvars = ()
# Test fn.__code__.co_freevars
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 1, b'', ())
fn.__code__.co_freevars = ()
# Test fn.__code__.co_names
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 1, b'', ())
fn.
