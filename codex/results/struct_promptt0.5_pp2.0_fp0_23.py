import _struct
# Test _struct.Struct.

def check(fmt, expected, value):
    s = _struct.Struct(fmt)
    got = s.pack(value)
    if got != expected:
        raise TestFailed, '%s: expected %r, got %r' % (fmt, expected, got)
    try:
        got = s.pack_into(bytearray(s.size), 0, value)
    except TypeError:
        pass
    else:
        got = bytes(got)
        if got != expected:
            raise TestFailed, '%s: expected %r, got %r' % (fmt, expected, got)
    got, = s.unpack(expected)
    if got != value:
        raise TestFailed, '%s: expected %r, got %r' % (fmt, value, got)
    try:
        got, = s.unpack_from(expected, 0)
    except TypeError:
        pass
    else:
        if got != value:
            raise TestFailed, '%s: expected %r, got
