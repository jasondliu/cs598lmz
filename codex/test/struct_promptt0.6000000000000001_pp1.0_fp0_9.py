import _struct
# Test _struct.Struct.
s = _struct.Struct('hhl')
values = (1, 2, 3)
print(s.pack(*values))
print(s.unpack(s.pack(*values)))
print(s.size)
print(s.format)
print(s.unpack_from(b'\x01\x00\x02\x00\x03\x00\x04\x00', 2))
print(s.pack_into(bytearray(8), 2, *values))
# Test _struct.Struct.iter_unpack.
s = _struct.Struct('hhl')
print(list(s.iter_unpack(b'\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00\x06\x00\x07\x00\x08\x00')))
# Test _struct.Struct.iter_unpack with buffer.
s = _struct.Struct('hhl')
