import _struct
# Test _struct.Struct.
# Test packing.
s = _struct.Struct('hhl')
str(s)
s.size
s.pack(1, 2, 3)
s.pack_into(b'xxxxx', 5, 1, 2, 3)
s.unpack(s.pack(1, 2, 3))
s.unpack_from(s.pack(1, 2, 3), 0)
s.iter_unpack(s.pack(1, 2, 3))
s.iter_unpack(s.pack(1, 2, 3), 0)
# Test unpacking.
s = _struct.Struct('hhl')
s.unpack(b'\x01\x00\x02\x00\x03\x00\x00\x00')
s.unpack_from(b'xxxxx\x01\x00\x02\x00\x03\x00\x00\x00', 5)
s.iter_unpack(b'\x01\x00\x02\x00\x03\x00\x00\x00')

