import _struct
# Test _struct.Struct.unpack_from()

# Create a Struct object
fmt = 'hhl'
s = _struct.Struct(fmt)

# Create a buffer
buf = array.array('b', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Unpack the buffer
print(s.unpack_from(buf, offset=2))
