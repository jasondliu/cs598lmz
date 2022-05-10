import _struct
# Test _struct.Struct

def test(typecode, format, expected):
    s = _struct.Struct(typecode)
    assert s.format == format
    assert s.size == struct.calcsize(format)
    assert s.pack(expected) == struct.pack(format, expected)
    assert s.unpack(s.pack(expected)) == (expected,)
    assert s.unpack_from(s.pack(expected), 0) == (expected,)

test('x', 'x', 0)
test('c', 'c', b'x')
test('b', 'b', 0)
test('b', 'b', 127)
test('B', 'B', 0)
test('B', 'B', 255)
test('h', 'h', 0)
test('h', 'h', 32767)
test('H', 'H', 0)
test('H', 'H', 65535)
test('i', 'i', 0)
test('i', 'i', 2147483647)
test('I', 'I', 0)
