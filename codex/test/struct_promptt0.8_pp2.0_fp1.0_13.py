import _struct
# Test _struct.Struct class
# Test _struct.Struct.pack
fmt = 'HHI'
s = _struct.Struct(fmt)
bs = s.pack(1,2,3)
print(s.size)
print(bs)
# Test _struct.Struct.unpack
us = s.unpack(bs)
print(us)
# Test _struct.Struct.iter_unpack
print(list(s.iter_unpack(bs)))
# Test _struct.Struct.pack_into
by = bytearray(b'abcde')
s.pack_into(by, 1, 1,2,3)
print(by)
# Test _struct.Struct.unpack_from
print(s.unpack_from(by, 1))
# Test _struct.Struct.iter_unpack_from
