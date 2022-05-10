fn = lambda: None
# Test fn.__code__.co_firstlineno:
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 1, b'', (), (), ())

# Test fn.__code__.co_varnames:
def fn(): pass
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', ('x',), (), (), '', '', 1, b'', (), (), ())

# Test fn.__code__.co_argcount:
def fn(): pass
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 1, b'', (), (), ())

# Test fn.__code__.co_flags:
def fn(): pass
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 1, b'', (), (), ())

# Test fn.__code__.co_flags & 0x08:
def fn(): pass
fn.__code__ = types.Code
