import _struct
# Test _struct.Struct.format_size
assert _struct.Struct('i').format_size() == 4
assert _struct.Struct('ii').format_size() == 8
# Test _struct.Struct.size
assert _struct.Struct('i').size == 4
assert _struct.Struct('ii').size == 8
# Test _struct.Struct.pack
assert _struct.Struct('i').pack(1) == b'\x01\x00\x00\x00'
assert _struct.Struct('ii').pack(1, 2) == b'\x01\x00\x00\x00\x02\x00\x00\x00'
# Test _struct.Struct.unpack
assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,)
assert _struct.Struct('ii').unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00') == (1, 2)
# Test _struct.Struct.iter_unpack
assert list(_struct.Struct('i').
