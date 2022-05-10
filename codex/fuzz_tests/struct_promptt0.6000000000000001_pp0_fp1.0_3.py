import _struct
# Test _struct.Struct
assert _struct.Struct('i').size == _struct.calcsize('i')
assert _struct.Struct('i').pack(42) == _struct.pack('i', 42)
assert _struct.Struct('i').unpack(_struct.pack('i', 42)) == (42,)

# Test _struct.Struct.iter_unpack
assert list(_struct.Struct('ii').iter_unpack([b'\x01\x00\x00\x00\x02\x00\x00\x00'])) == [(1, 2)]
assert list(_struct.Struct('ii').iter_unpack([b'\x01\x00\x00\x00\x02\x00\x00\x00', b'\x03\x00\x00\x00'])) == [(1, 2), (3, 0)]
assert list(_struct.Struct('ii').iter_unpack([b'\x01\x00\x00\x00\x02\x00\x00\x00', b'\x03\x00\x00\x00\x
