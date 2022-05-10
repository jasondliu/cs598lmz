import _struct
# Test _struct.Struct

# basic test
st = _struct.Struct('i')
st.size
st.pack(0)
st.pack(0, 1)
st.pack(1, 2)
st.pack(1, 2, 3)
# st.pack(1, 2, 3, 4)
st.pack_into(bytearray(10), 0, 0)
st.pack_into(bytearray(10), 2, 0)
st.pack_into(bytearray(10), 4, 0)
st.pack_into(bytearray(10), 6, 0)
st.pack_into(bytearray(10), 8, 0)
# st.pack_into(bytearray(10), 10, 0)
st.unpack(b'\x00\x00\x00\x00')
st.unpack_from(b'\x00\x00\x00\x00', 0)
st.unpack_from(b'\x00\x00\x00\x00', 2)
st.unpack_from
