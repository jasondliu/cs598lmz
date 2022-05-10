import _struct
# Test _struct.Struct

# Test _struct.Struct with big endian format strings
s = _struct.Struct(">i")
assert s.size == 4
assert s.pack(1) == b"\x00\x00\x00\x01"
assert s.unpack(b"\x00\x00\x00\x01") == (1,)

s = _struct.Struct(">ii")
assert s.size == 8
assert s.pack(1, 2) == b"\x00\x00\x00\x01\x00\x00\x00\x02"
assert s.unpack(b"\x00\x00\x00\x01\x00\x00\x00\x02") == (1, 2)

s = _struct.Struct(">iii")
assert s.size == 12
assert s.pack(1, 2, 3) == b"\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03"
assert s.unpack
