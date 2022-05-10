import _struct
# Test _struct.Struct.

# Create a struct object.
s = _struct.Struct("i")
# Create a buffer.
b = s.pack(1)
# Unpack the buffer.
print s.unpack(b)

# Create a struct object.
s = _struct.Struct("if")
# Create a buffer.
b = s.pack(1, 1.0)
# Unpack the buffer.
print s.unpack(b)

# Create a struct object.
s = _struct.Struct("i")
# Create a buffer.
b = s.pack(1)
# Unpack the buffer.
print s.unpack_from(b, 0)

# Create a struct object.
s = _struct.Struct("i")
# Create a buffer.
b = s.pack(1)
# Unpack the buffer.
print s.unpack_from(b, 0, 1)

# Create a struct object.
s = _struct.Struct("if")
# Create a buffer.
b = s.pack(1, 1.0)
# Unpack the buffer.

