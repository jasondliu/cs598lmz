import _struct
# Test _struct.Struct.

def unpack_test(fmt, data):
    s = _struct.Struct(fmt)
    print(s.unpack(data))

def pack_test(fmt, *data):
    s = _struct.Struct(fmt)
    print(s.pack(*data))

print('Unpacking')
unpack_test('hhl', b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00')
unpack_test('hhl', bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'))
unpack_test('hhl', memoryview(b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'))

print('Packing')
pack_test('hhl', 1, 2, 3)
pack
