import _struct
# Test _struct.Struct

# Test packing
s = _struct.Struct('hhl')

# Test native packing
print(s.pack(1, 2, 3))

# Test native packing with buffer
print(s.pack_into(bytearray(12), 0, 1, 2, 3))

# Test native packing with buffer and offset
print(s.pack_into(bytearray(12), 4, 1, 2, 3))

# Test native unpack
print(s.unpack(b'\x01\x00\x02\x00\x03\x00\x00\x00'))

# Test native unpack_from
print(s.unpack_from(b'\x01\x00\x02\x00\x03\x00\x00\x00', 0))

# Test native unpack_from with offset
print(s.unpack_from(b'xxxx\x01\x00\x02\x00\x03\x00\x00\x00', 4))

# Test native size
print(s.size)
