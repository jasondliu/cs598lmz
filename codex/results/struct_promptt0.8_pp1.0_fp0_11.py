import _struct
# Test _struct.Struct
st = _struct.Struct("xxxb")
st.size
# Test _struct.pack
st.pack(0, 1, 2, 3)
st.unpack(st.pack(0, 1, 2, 3))
# Test _struct.pack_into
buf = bytes(4)
st.pack_into(buf, 0, 0, 1, 2, 3)
st.unpack(buf)
st.pack_into(buf, 0, 0, 1, 2, 4)
st.unpack(buf)
# Test _struct.calcsize
st1 = _struct.Struct("b")
st1.calcsize()
# Test _struct.unpack_from
st1.unpack_from(b"123", 1)
st1.unpack_from(b"12")
# Test _struct.iter_unpack
# Test iter_unpack with buffer
list(st.iter_unpack(buf))
# Test iter_unpack with bytes
iter_unpack_bytes = st.iter_unpack(_memview(buf))
next(iter_unpack
