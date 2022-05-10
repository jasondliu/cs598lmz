import _struct
# Test _struct.Struct

# Create a struct object
st = _struct.Struct("hhi")

# Create a buffer to hold the packed data
buf = _struct.create_string_buffer(st.size)

# Pack some data into the buffer
print st.pack_into(buf, 0, 1, 2, 3)

# Unpack the data in the buffer
print st.unpack_from(buf, 0)

# Create a struct object
st = _struct.Struct("hhl")

# Create a buffer to hold the packed data
buf = _struct.create_string_buffer(st.size)

# Pack some data into the buffer
print st.pack_into(buf, 0, 1, 2, 3)

# Unpack the data in the buffer
print st.unpack_from(buf, 0)

# Create a struct object
st = _struct.Struct("hhh")

# Create a buffer to hold the packed data
buf = _struct.create_string_buffer(st.size)

# Pack some data into the buffer
print st.pack_into(buf, 0, 1
