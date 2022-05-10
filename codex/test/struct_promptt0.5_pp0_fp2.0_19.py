import _struct
# Test _struct.Struct.

# Create a struct object.
s = _struct.Struct("i")
# Create a buffer.
b = s.pack(1)
# Unpack the buffer.
