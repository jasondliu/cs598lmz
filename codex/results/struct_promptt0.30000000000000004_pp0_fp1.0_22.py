import _struct
# Test _struct.Struct()

def test_struct(typecode, size, format):
    s = _struct.Struct(typecode)
    assert s.size == size
    assert s.format == format
    assert repr(s) == "<_struct.Struct object at %x>" % id(s)
    assert s.pack(42) == _struct.pack(typecode, 42)
    assert s.pack_into(bytearray(s.size), 0, 42) == _struct.pack_into(typecode, bytearray(s.size), 0, 42)
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack_from(s.pack(42), 0) == (42,)
    assert s.unpack_from(bytearray(s.size), 0) == (0,)
    assert s.iter_unpack(s.pack(42)) == iter((42,))
    assert s.iter_unpack(bytearray(s.size)) == iter((0,))
    assert s.iter_unpack(byt
