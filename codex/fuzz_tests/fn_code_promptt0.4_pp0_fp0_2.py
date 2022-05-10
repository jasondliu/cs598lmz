fn = lambda: None
# Test fn.__code__.co_argcount == 0
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
# Test fn.__code__.co_varnames == ()
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
# Test fn.__code__.co_argcount > 0
fn.__code__ = types.CodeType(1, 0, 0, 0, b'', ('a',), (), (), '', '', 0, b'')
# Test fn.__code__.co_varnames > 0
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), ('a',), (), '', '', 0, b'')
# Test fn.__code__.co_argcount > 0 and fn.__code__.co_varnames > 0
fn.__code__ = types.CodeType(1, 0, 0, 0, b'', ('a',
