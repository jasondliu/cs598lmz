import _struct
# Test _struct.Struct

# Create a simple format
fmt = _struct.Struct('hhl')

# Create a buffer
buf = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Unpack the buffer
print(fmt.unpack(buf))

# Create a new buffer
buf = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Unpack the buffer using an offset and size
print(fmt.unpack_from(buf, 2))

# Create a new buffer
buf = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Pack values into the buffer
print(fmt.pack(1, 2, 3))

# Create a new buffer
buf = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Pack values into a buffer using an offset
print(fmt.pack_into(buf, 2, 1, 2, 3))

# Create a new buffer
buf = bytes([
