import _struct
# Test _struct.Struct

# Create a struct object
st = _struct.Struct("hhi")

# Create a buffer to hold the packed data
buf = _struct.create_string_buffer(st.size)

# Pack some data into the buffer
