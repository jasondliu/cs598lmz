fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'')
fn()
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'x')
fn()
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'x,y')
fn()
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'x,y,z')
fn()
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(0, 0,
