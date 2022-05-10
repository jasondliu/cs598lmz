import _struct
# Test _struct.Struct.unpack_from

import _struct

def test(fmt, data):
    s = _struct.Struct(fmt)
    print(s.unpack_from(data))

test('!H', b'\x01\x02')
test('!H', b'\x01\x02\x03')
test('!H', b'\x01\x02\x03\x04')
test('!H', b'\x01\x02\x03\x04\x05')
test('!H', b'\x01\x02\x03\x04\x05\x06')
test('!H', b'\x01\x02\x03\x04\x05\x06\x07')
test('!H', b'\x01\x02\x03\x04\x05\x06\x07\x08')
test('!H', b'\x01\x02\x03\x04\x05\x06\x07\x08\x09')
