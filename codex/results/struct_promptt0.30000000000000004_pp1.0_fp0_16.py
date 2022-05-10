import _struct
# Test _struct.Struct

# Create a struct object
s = _struct.Struct('hhl')

# Create a buffer to pack into
buf = _array.array('c', '\0' * s.size)

# Pack some values into the buffer
s.pack_into(buf, 0, 1, 2, 3)

# Unpack the values back into Python variables
x, y, z = s.unpack_from(buf, 0)

print x, y, z
