import _struct
# Test _struct.Struct.unpack_from() method
s = _struct.Struct('hhh')
v = memoryview(b'2\x00\xfd\xff\x03\x00\xfe\xff')
assert s.unpack_from(v, 0) == (2, -3)
assert s.unpack_from(v, 1) == (511, -2)
assert s.unpack_from(v, 2) == (1022, -1)
assert s.unpack_from(v, 3) == (1533, 0)
assert s.unpack_from(v, 4) == (2044, 1)
assert s.unpack_from(v, 5) == (2555, 2)
assert s.unpack_from(v, 6) == (3066, 3)
assert s.unpack_from(v, 7) == (3577, 4)
# Test _struct.Struct.pack_into() method
s = _struct.Struct('hhh')
v = memoryview(bytearray(8))
