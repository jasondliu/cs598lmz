import _struct
# Test _struct.Struct methods.
s = _struct.Struct('i4shh')
# .pack
assert s.pack(12345, 'abcd', 1, 2) == b'\x39\x30\x00\x00abcd\x00\x01\x02'
assert s.pack(12345, 'abcd', 1, 2) == s.pack_into(bytearray(s.size), 0,
      12345, 'abcd', 1, 2)
assert s.pack(12345, 'abcd', 1, 2) == s.pack_into(memoryview(bytearray(s.size)), 0,
      12345, 'abcd', 1, 2)
assert s.pack(12345, 'abcd', 1, 2) == s.pack_into(memoryview(bytearray(s.size)), 0,
      12345, 'abcd', 1, 2)
# .unpack
assert s.unpack(b'\x39\x30\x00\x00abcd\x00\x01\x02') == (12345,
