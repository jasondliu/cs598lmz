import _struct
# Test _struct.Struct.pack_into() and unpack_from()

# Create a Struct object
s = _struct.Struct('hhl')

# Create a buffer
buf = _array.array('b', b'\0' * s.size)

# Pack some data into the buffer
s.pack_into(buf, 0, 1, 2, 3)

# Unpack the data into 3 variables
a, b, c = s.unpack_from(buf, 0)

print(a, b, c)

# Pack again into the buffer, overwriting the previous data
s.pack_into(buf, 0, 4, 5, 6)

# Unpack again
a, b, c = s.unpack_from(buf, 0)

print(a, b, c)

# Pack again into the buffer, overwriting the previous data
s.pack_into(buf, 0, b'abc')

# Unpack again
a, b, c = s.unpack_from(buf, 0)

print(a, b, c)
