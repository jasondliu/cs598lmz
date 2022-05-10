import _struct
# Test _struct.Struct().
s = _struct.Struct('i')
assert s.size == _struct.calcsize('i') == 4
assert s.format == 'i'
assert s.pack(1) == b'\x01\x00\x00\x00'
assert s.unpack(b'\x01\x00\x00\x00') == (1,)
assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
assert s.unpack_from(b'\x01\x00\x00\x00', 1) == (0,)
# Test _struct.Struct().__new__().
assert _struct.Struct('i') is _struct.Struct('i')
assert _struct.Struct('i') is not _struct.Struct('I')
assert _struct.Struct('i') is not _struct.Struct('ii')
# Test _struct.Struct().__repr__().
assert repr
