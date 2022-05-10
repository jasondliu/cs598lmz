import _struct
# Test _struct.Struct()

def test_struct(typecode, size):
    fmt = _struct.Struct(typecode)
    assert fmt.size == size
    assert fmt.format == typecode
    assert fmt.unpack(b'\0'*size) == (0,)
    assert fmt.unpack_from(b'\0'*size) == (0,)
    assert fmt.unpack_from(b'\0'*size, 0) == (0,)
    assert fmt.unpack_from(bytearray(b'\0'*size), 0) == (0,)
    assert fmt.pack(0) == b'\0'*size
    assert fmt.pack_into(bytearray(b'\0'*size), 0, 0) is None
    assert fmt.pack_into(b'\0'*size, 0, 0) is None
    assert fmt.pack_into(bytearray(b'\0'*size), 0, 0) is None
    assert fmt.pack_into(b'\0'*size, 0, 0) is None
