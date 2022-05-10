import _struct
# Test _struct.Struct.

# Create a binary packing format string.
fmt = 'I 2s f'
# Get a struct object.
s = _struct.Struct(fmt)
# Pack the data into a buffer.
buf = s.pack(1, 'ab', 2.7)
# Unpack the buffer.
print s.unpack(buf)

# Create a binary packing format string.
fmt = 'hhl'
# Get a struct object.
s = _struct.Struct(fmt)
# Pack the data into a buffer.
buf = s.pack(1, 2, 3)
# Unpack the buffer.
print s.unpack(buf)

# Create a binary packing format string.
fmt = 'hhl'
# Get a struct object.
s = _struct.Struct(fmt)
# Pack the data into a buffer.
buf = s.pack(1, 2, 3)
# Unpack the buffer.
print s.unpack(buf)

# Create a binary packing format string.
fmt = 'hhl'
# Get a struct object.
s =
