import _struct
# Test _struct.Struct as a freestanding function

def test_struct():
    TEST_STRING = "testing..."
    s = _struct.Struct("i 7s")
    packed = s.pack(123, TEST_STRING)
    unpacked = s.unpack(packed)
    assert unpacked == (123, TEST_STRING)
    assert s.size == _struct.calcsize(s.format)
    assert s.format == "i 7s"
    assert str(s) == "<class '_struct.Struct'>"

def test_pack_into():
    s = _struct.Struct("i7s")
    b = bytearray(s.size)
    s.pack_into(b, 0, 123, b"testing")
    assert s.unpack_from(b, 0) == (123, b"testing")

def test_unpack_from():
    s = _struct.Struct("i7s")
    b = s.pack(123, b"testing")
    assert s.unpack_from(b, 0) == (123, b"
