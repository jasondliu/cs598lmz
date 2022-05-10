import _struct
# Test _struct.Struct.unpack
print(st.unpack(data))
print(st.unpack_from(data, 2))
data = bytearray(data)
st.unpack_into(data, 0, 1.0, 2.0)
print(data, 1.0, 2.0)
