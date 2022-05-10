import _struct
# Test _struct.Struct.format_size
assert _struct.Struct("i").format_size("<i") == _struct.Struct("<i").size
assert _struct.Struct("i").format_size("<I") == _struct.Struct("<I").size
assert _struct.Struct("i").format_size("<i") == _struct.Struct("<i").size
assert _struct.Struct("i").format_size("<I") == _struct.Struct("<I").size

# Test _struct.Struct.size
assert _struct.Struct("i").size == 4
assert _struct.Struct("I").size == 4
assert _struct.Struct("<i").size == 4
assert _struct.Struct("<I").size == 4
assert _struct.Struct(">i").size == 4
assert _struct.Struct(">I").size == 4

# Test _struct.Struct.pack
assert _struct.Struct("i").pack(1) == b'\x01\x00\x00\x00'
