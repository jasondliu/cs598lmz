import _struct
# Test _struct.Struct.pack_into() and _struct.Struct.unpack_from()

# This is the endian and size of the platform
ENDIAN = sys.byteorder == 'little'
SIZE_32 = _struct.calcsize("&lt;l")
SIZE_64 = _struct.calcsize("&lt;q")

# Test our endian assumptions.
assert _struct.pack("&lt;i", 1) == _struct.pack("&gt;i", 1)
assert _struct.pack("=i", 1) == _struct.pack("&gt;i", 1)
assert _struct.unpack("&lt;i", "\1\0\0\0")[0] == 1
assert _struct.unpack("&gt;i", "\0\0\0\1")[0] == 1
assert _struct.unpack("=i", "\0\0\0\1")[0] == 1

# Test that pack() is equivalent to pack_into() with a zero-length buffer.
buf = bytearray(10)
