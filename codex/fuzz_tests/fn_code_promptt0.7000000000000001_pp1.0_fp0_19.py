fn = lambda: None
# Test fn.__code__.co_flags
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b''
)

# Test sys._getframe
# .f_code
sys._getframe().f_code = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b''
)
# .f_locals
sys._getframe().f_locals = {}

# Test types.CodeType
types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'')

# Test types.FrameType
types.FrameType(
    None, '/tmp', 0, 0, None,
    (), (), (), '', None, None, None
)

# Test types.TracebackType
types.TracebackType(None, None, None)

# Test types.MappingProxyType
__builtins__.__dict__ = {}
types.M
