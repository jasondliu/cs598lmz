import _struct
# Test _struct.Struct

# Test the basic operations
s = _struct.Struct("i")

# Test that the format string is stored
assert s.format == "i"

# Test that the size is calculated
assert s.size == _struct.calcsize("i")

# Test that packing works
assert s.pack(1) == b"\x01\x00\x00\x00"

# Test that unpacking works
assert s.unpack(b"\x01\x00\x00\x00") == (1,)

# Test that iter unpacking works
assert tuple(s.iter_unpack(b"\x01\x00\x00\x00\x02\x00\x00\x00")) == (1, 2)

# Test that pack_into works
buf = bytearray(8)
s.pack_into(buf, 0, 1)
assert buf == b"\x01\x00\x00\x00\x00\x00\x00\x00"

# Test that unpack_from works
assert s.un
