import _struct
# Test _struct.Struct with a big endian format
big_endian = _struct.Struct(">i")
big_endian.pack(0x12345678)

# Test _struct.Struct with a little endian format
little_endian = _struct.Struct("<i")
little_endian.pack(0x12345678)

# Test _struct.Struct with a native format
native = _struct.Struct("=i")
native.pack(0x12345678)

# Test _struct.Struct with a native format and a specified size
native_size = _struct.Struct("=i", 4)
native_size.pack(0x12345678)

# Test _struct.Struct with a native format and a specified alignment
native_align = _struct.Struct("=i", 4, 1)
native_align.pack(0x12345678)

# Test _struct.Struct with a native format, a specified size and a specified alignment
native_align_size = _struct.Struct("=i", 4, 1)
native_align_size.pack(0x12345678)
