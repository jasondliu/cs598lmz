import _struct
# Test _struct.Struct
# This is pure Python code
#

def _test(fmt, args, expected):
    # test struct.pack
    s = _struct.Struct(fmt)
    got = s.pack(*args)
    if got != expected:
        raise ValueError("pack(%r) returned %r" % (args, got))
    # test struct.unpack
    args2 = s.unpack(expected)
    if args2 != args:
        raise ValueError("unpack(%r) returned %r" % (expected, args2))
    # test struct.calcsize
    size = s.size
    if size != len(expected):
        raise ValueError("calcsize() returned %d" % size)
    # test struct.iter_unpack
    args3 = tuple(s.iter_unpack(expected))
    if args3 != args:
        raise ValueError("iter_unpack(%r) returned %r" % (expected, args3))

_test("cc", (12, 56), b"\x0c8")

_test("
