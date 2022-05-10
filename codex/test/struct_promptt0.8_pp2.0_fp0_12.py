import _struct
# Test _struct.Struct

# First create some small Struct objects.

# S is big enough to hold an integer
fmt = "I"
expected_size = _struct.calcsize(fmt)
s = _struct.Struct(fmt)

eq(s.size, expected_size)

# Make a mutable buffer
buf = bytearray(expected_size)

# Try packing
s.pack_into(buf, 0, 1)

# Try unpacking
eq(s.unpack_from(buf, 0), (1,))

# Test with fill character

# S is big enough to hold an integer
fmt = "I"
expected_size = _struct.calcsize(fmt)
s = _struct.Struct(fmt, fill="X")

eq(s.size, expected_size)

# Make a mutable buffer
buf = bytearray(expected_size)

# Try packing
s.pack_into(buf, 0, 1)

# Try unpacking
