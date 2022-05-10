import _struct
# Test _struct.Struct

def test_struct_error():
    # Issue #5462: _struct.error should be a subclass of ValueError
    assert issubclass(_struct.error, ValueError)

def test_struct_pack_unpack():
    # Issue #5463: struct.pack/unpack should return bytes
    assert isinstance(_struct.pack('i', 1), bytes)
    assert isinstance(_struct.unpack('i', b'12345678')[0], int)

def test_struct_unpack_from():
    # Issue #5464: struct.unpack_from should return bytes
    assert isinstance(_struct.unpack_from('i', b'12345678', offset=2)[0], int)

def test_struct_pack_into():
    # Issue #5465: struct.pack_into should return None
    assert _struct.pack_into('i', bytearray(10), 2, 12345678) is None

