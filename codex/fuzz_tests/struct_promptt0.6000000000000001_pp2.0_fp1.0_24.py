import _struct
# Test _struct.Struct with non-native byte order
def test(format, value):
    native = _struct.Struct(format)
    other = _struct.Struct(format + '<')
    s = native.pack(*value)
    assert other.unpack(s) == value
    s = native.pack_into(bytearray(native.size), 0, *value)
    assert other.unpack_from(s, 0) == value
    s = native.pack_into(memoryview(bytearray(native.size)), 0, *value)
    assert other.unpack_from(s, 0) == value
    buf = bytearray(other.size)
    other.pack_into(buf, 0, *value)
    assert native.unpack_from(buf, 0) == value
    buf = bytearray(other.size)
    other.pack_into(memoryview(buf), 0, *value)
    assert native.unpack_from(buf, 0) == value
test('bBhHiIlLqQfd', (0, 1, -1,
