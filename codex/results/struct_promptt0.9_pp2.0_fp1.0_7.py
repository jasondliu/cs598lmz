import _struct
# Test _struct.Struct.unpack
print(st.unpack(data))
print(st.unpack_from(data, 2))
data = bytearray(data)
st.unpack_into(data, 0, 1.0, 2.0)
print(data, 1.0, 2.0)
</code>
Note: when using <code>unpack_from</code> the <code>offset</code> represents the start position in the byte string. If <code>offset</code> is omitted then the first character from the byte string is used. Using tuple assignment the values at the start position of the byte string are replaced.

