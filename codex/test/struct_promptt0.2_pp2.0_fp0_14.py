import _struct
# Test _struct.Struct

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.size == struct.calcsize(fmt)
    assert s.format == fmt
    assert s.unpack(s.pack(*expected)) == expected

def test_struct_error(fmt):
    s = _struct.Struct(fmt)
    raises(struct.error, s.pack)

def test_struct_unpack_error(fmt, data):
    s = _struct.Struct(fmt)
    raises(struct.error, s.unpack, data)

def test_struct_iter_unpack_error(fmt, data):
    s = _struct.Struct(fmt)
    raises(struct.error, s.iter_unpack, data)

def test_struct_pack_into_error(fmt, data, offset):
    s = _struct.Struct(fmt)
    raises(struct.error, s.pack_into, data, offset)

