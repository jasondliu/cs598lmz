import _struct
# Test _struct.Struct.unpack()

def test(fmt, data):
    s = _struct.Struct(fmt)
    print(s.unpack(data))

test('i', b'\x00\x00\x00\x00')
test('i', b'\x00\x00\x00\x01')
test('i', b'\x00\x00\x00\x02')
test('i', b'\x00\x00\x00\x04')
test('i', b'\x00\x00\x00\x08')
test('i', b'\x00\x00\x00\x10')
test('i', b'\x00\x00\x00\x20')
test('i', b'\x00\x00\x00\x40')
test('i', b'\x00\x00\x00\x80')
test('i', b'\x00\x00\x00\xFF')
test('i', b'\x00\x00\x00\x
