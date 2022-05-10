import _struct
# Test _struct.Struct.

# _struct.Struct.__init__()
assert _struct.Struct('i').size == 4
assert _struct.Struct('i').format == 'i'
assert _struct.Struct('ii').size == 8
assert _struct.Struct('ii').format == 'ii'

# _struct.Struct.pack()
assert _struct.Struct('i').pack(1) == b'\x01\x00\x00\x00'
assert _struct.Struct('ii').pack(1, 2) == b'\x01\x00\x00\x00\x02\x00\x00\x00'
assert _struct.Struct('ii').pack(1) == b'\x01\x00\x00\x00\x00\x00\x00\x00'
assert _struct.Struct('ii').pack(1, 2, 3) == b'\x01\x00\x00\x00\x02\x00\x00\x00'

# _struct.Struct.unpack()
