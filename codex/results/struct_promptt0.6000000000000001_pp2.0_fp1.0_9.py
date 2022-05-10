import _struct
# Test _struct.Struct
import struct

# Test _struct.pack
print(_struct.pack('hhl', 1, 2, 3))
print(struct.pack('hhl', 1, 2, 3))

# Test _struct.pack_into
b = bytearray(24)
print(_struct.pack_into('hhl', b, 0, 1, 2, 3))
print(struct.pack_into('hhl', b, 0, 1, 2, 3))

# Test _struct.unpack
print(_struct.unpack('hhl', b'\x01\x00\x02\x00\x03\x00\x00\x00'))
print(struct.unpack('hhl', b'\x01\x00\x02\x00\x03\x00\x00\x00'))

# Test _struct.unpack_from
print(_struct.unpack_from('hhl', b'\x01\x00\x02\x00\x03\x00\x00\x00', 2))
print(struct.unpack_from
