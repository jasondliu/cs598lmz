import _struct
# Test _struct.Struct

# Test the basic constructors
st = _struct.Struct('i')
st = _struct.Struct('i',)
st = _struct.Struct('i', 'little')
st = _struct.Struct('i', 'big')

# Test the format string
st = _struct.Struct('i')
st.format
st = _struct.Struct('ii')
st.format
st = _struct.Struct('i'*100)
st.format

# Test the size
st = _struct.Struct('i')
st.size
st = _struct.Struct('ii')
st.size
st = _struct.Struct('i'*100)
st.size

# Test pack
st = _struct.Struct('i')
st.pack(1)
st = _struct.Struct('ii')
st.pack(1, 2)
st = _struct.Struct('i'*100)
st.pack(*range(100))

# Test unpack
st = _struct.Struct('i')
st.unpack(st.pack(1))
st = _struct.Struct
