import _struct
# Test _struct.Struct
assert _struct.Struct('@I')(42).size == 4
# Test _struct.Struct.unpack
assert _struct.Struct('@I').unpack(b'\x00\x00\x00*') == (42,)
# Test _struct.Struct.pack
assert _struct.Struct('@I').pack(42) == b'\x00\x00\x00*'

# Test _struct.calcsize
assert _struct.calcsize('@I') == 4

# Test _struct.pack
assert _struct.pack('@I', 42) == b'\x00\x00\x00*'

# Test _struct.unpack
assert _struct.unpack('@I', b'\x00\x00\x00*') == (42,)

# Test _struct.pack_into
