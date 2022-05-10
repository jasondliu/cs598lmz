import _struct
# Test _struct.Struct.
assert _struct.Struct('i').size == 4
assert _struct.Struct('i').pack(42) == b'*\x00\x00\x00'
assert _struct.Struct('i').unpack(b'*\x00\x00\x00') == (42,)
# Test _struct.pack.
assert _struct.pack('i', 42) == b'*\x00\x00\x00'
# Test _struct.unpack.
assert _struct.unpack('i', b'*\x00\x00\x00') == (42,)
# Test _struct.calcsize.
assert _struct.calcsize('i') == 4

# Test _struct.Struct.
assert _struct.Struct('<i').size == 4
assert _struct.Struct('<i').pack(42) == b'*\x00\x00\x00'
assert _struct.Struct('<i').unpack(b'*\x00\x00\x00') == (42,)
# Test _struct.pack.
assert _struct.pack('
