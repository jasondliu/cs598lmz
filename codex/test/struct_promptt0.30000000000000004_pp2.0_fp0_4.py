import _struct
# Test _struct.Struct

# Create a struct with a format string
s = _struct.Struct('hhl')

# Create a buffer to hold the packed data
buffer = bytes(s.size)

# Pack some data into the buffer
s.pack_into(buffer, 0, 1, 2, 3)

# Unpack the buffer into a tuple
print(s.unpack_from(buffer, 0))

# Unpack the buffer into a tuple, starting at offset 2
print(s.unpack_from(buffer, 2))

# Unpack the buffer into a tuple, starting at offset 4
print(s.unpack_from(buffer, 4))

# Unpack the buffer into a tuple, starting at offset 6
print(s.unpack_from(buffer, 6))

# Unpack the buffer into a tuple, starting at offset 8
print(s.unpack_from(buffer, 8))

# Unpack the buffer into a tuple, starting at offset 10
