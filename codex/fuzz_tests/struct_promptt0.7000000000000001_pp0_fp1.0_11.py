import _struct
# Test _struct.Struct class.

TestError = _struct.error

def test_struct():
    # Test struct object creation
    s = _struct.Struct("i")
    if repr(s).find("Format string: 'i'") < 0:
        raise TestError("repr of struct object failed")
    if s.format != "i":
        raise TestError("struct object initialization failed")
    # Test pack
    x = 0x12345678
    y = 12345678
    z = 0x1234abcd
    f = 1.25
    p = s.pack(x)
    if p != b"x\xbcV\x12":
        raise TestError("incorrect string returned by pack")
    p = s.pack(y)
    if p != b"x\xbcV\x12":
        raise TestError("incorrect string returned by pack")
    # Test unpack
    if s.unpack(b"x\xbcV\x12") != (x,):
        raise TestError("incorrect values returned by unpack")
    # Test pack with buffer
