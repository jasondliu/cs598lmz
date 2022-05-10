import _struct
# Test _struct.Struct

def test_struct_unpack():
    struct = _struct.Struct('i')
    assert struct.unpack(b'\0\0\0\0') == (0,)
    assert struct.unpack(b'\0\0\0\1') == (1,)
    assert struct.unpack(b'\0\0\0\2') == (2,)
    assert struct.unpack(b'\0\0\xff\xff') == (-1,)
    assert struct.unpack(b'\0\0\xff\xfe') == (-2,)
    assert struct.unpack(b'\xff\xff\xff\xff') == (-1,)
    assert struct.unpack(b'\xff\xff\xff\xfe') == (-2,)
    raises(struct.error, struct.unpack, b'\0\0\0')
    raises(struct.error, struct.unpack, b'\0\0\0\0\0')

def test_struct_pack():
    struct = _struct.Struct('i')
    assert struct
