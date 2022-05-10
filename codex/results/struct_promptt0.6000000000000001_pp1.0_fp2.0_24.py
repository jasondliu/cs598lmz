import _struct
# Test _struct.Struct.
s = _struct.Struct("x")

# Test _struct.unpack.
r = s.unpack(s.pack(1))
assert r == (1,)

# Test _struct.pack.
r = s.pack(1)
assert r == b"\x00\x00\x00\x00"

# Test _struct.calcsize.
r = s.calcsize()
assert r == 1

# Test _struct.Struct.__doc__.
assert s.__doc__.startswith("Compiled struct object")

# Test _struct.Struct.__repr__.
assert repr(s) == "<class '_struct.Struct'>"

# Test _struct.Struct.format.
assert s.format == "x"

# Test _struct.Struct.size.
assert s.size == 1

# Test _struct.Struct.alignment.
assert s.alignment == 1

# Test _struct.Struct.format_char.
assert s.format_char == "x"

# Test _struct.Struct.format
