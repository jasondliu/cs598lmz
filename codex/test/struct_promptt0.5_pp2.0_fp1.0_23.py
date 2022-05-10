import _struct
# Test _struct.Struct
s = _struct.Struct("I3sI")

# Test _struct.unpack
t = s.unpack(b"\0\0\0\0abc\0\0\0\1")
assert t == (0, b"abc", 1)

# Test _struct.pack
assert s.pack(0, b"abc", 1) == b"\0\0\0\0abc\0\0\0\1"

# Test _struct.unpack_from
t = s.unpack_from(b"\0\0\0\0abc\0\0\0\1\0\0\0\2")
assert t == (0, b"abc", 1)

# Test _struct.calcsize
assert s.size == 12

# Test _struct.pack_into
s.pack_into(b"\0"*12, 0, 0, b"abc", 1)
assert b"\0"*12 == b"\0\0\0\0abc\0\0\0\1\0\0\0"
