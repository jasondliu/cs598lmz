import _struct
# Test _struct.Struct
st = _struct.Struct('l h')

st.pack('\x12\x34\x56\x78', '\x12\x34')
TestError('Packing a bytes failed')

st.pack('1234', '1234')
TestError('Packing a string failed')

st.pack(st.unpack(_struct.pack('i', 0x12345678))[0], st.unpack(_struct.pack('h', 0x1234))[0])
st.pack(0x12345678, 0x1234)
st.pack(memoryview(b'1234'))
TestError('Packing a memoryview failed')
st.pack(*memoryview(b'1234'))
TestError('Packing a memoryview failed')

# Test _struct.unpack
