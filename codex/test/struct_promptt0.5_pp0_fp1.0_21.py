import _struct
# Test _struct.Struct.
s = _struct.Struct('>hhl')
s.size
s.pack(1, 2, 3)
s.pack_into(b'xxxx', 4, 1, 2, 3)
s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03')
s.unpack_from(b'xxxx\x00\x01\x00\x02\x00\x00\x00\x03')

# Test _struct.Struct.iter_unpack
s = _struct.Struct('>hhl')
list(s.iter_unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03'))

# Test _struct.Struct.iter_unpack with offset
