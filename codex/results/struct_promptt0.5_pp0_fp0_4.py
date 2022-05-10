import _struct
# Test _struct.Struct.

def test_struct(fmt, expected, *args):
    s = _struct.Struct(fmt)
    got = s.pack(*args)
    if got != expected:
        raise ValueError("struct.pack(%r, %r) = %r, expected %r" %
                         (fmt, args, got, expected))
    got = s.unpack(expected)
    if got != args:
        raise ValueError("struct.unpack(%r, %r) = %r, expected %r" %
                         (fmt, expected, got, args))

def test_struct_error(fmt, expected, *args):
    s = _struct.Struct(fmt)
    try:
        got = s.pack(*args)
    except expected:
        pass
    else:
        raise ValueError("struct.pack(%r, %r) = %r, expected %r" %
                         (fmt, args, got, expected))
    try:
        got = s.unpack(expected)
    except expected:
        pass
    else
