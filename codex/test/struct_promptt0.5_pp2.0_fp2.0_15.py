import _struct
# Test _struct.Struct.

def test_struct(typecode):
    s = _struct.Struct(typecode)
    size = struct.calcsize(typecode)
    testdata = list(range(size))
    testdata = struct.pack(typecode, *testdata)
    unpacked = s.unpack(testdata)
    packed = s.pack(*unpacked)
    assert packed == testdata
    assert s.size == size
    assert s.format == typecode
    assert s.unpack_from(testdata) == unpacked
    assert s.pack_into(bytearray(size), 0, *unpacked) is None
    assert s.pack_into(bytearray(size), 0, *unpacked) == None
    assert s.pack_into(bytearray(size), 0, *unpacked) is None
    assert s.pack_into(bytearray(size), 0, *unpacked) == None
    assert s.unpack_from(testdata, 0) == unpacked
    assert s.unpack_from(testdata, 0)
