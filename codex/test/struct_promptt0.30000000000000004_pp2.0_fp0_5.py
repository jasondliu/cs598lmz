import _struct
# Test _struct.Struct

# Create a struct with format string 'hhl'
st = _struct.Struct('hhl')

# Create a buffer for the packed data
buf = _array.array('b', b'\0' * st.size)

# Pack 3 short integers and one long integer into the buffer
st.pack_into(buf, 0, 1, 2, 3, 4)

# Unpack the buffer contents into 4 integers
print(st.unpack_from(buf, 0))

# Create a struct with format string 'hhl'
st = _struct.Struct('hhl')

# Create a buffer for the packed data
buf = _array.array('b', b'\0' * st.size)

# Pack 3 short integers and one long integer into the buffer
st.pack_into(buf, 0, 1, 2, 3, 4)

# Unpack the buffer contents into 4 integers
print(st.unpack_from(buf, 0))

# Create a struct with format string 'hhl'
st = _struct.Struct('hhl')

# Create a buffer for the
