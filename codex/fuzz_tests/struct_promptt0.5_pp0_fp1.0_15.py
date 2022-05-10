import _struct
# Test _struct.Struct

# Create a struct object
st = _struct.Struct('i')

# Encode a tuple of values
t = (10,)
print(st.pack(*t))

# Encode a dictionary of names and values
d = {'x':10}
print(st.pack(**d))

# Encode a string buffer
s = st.pack('\0'*st.size)
print(s)

# Decode a string buffer
print(st.unpack(s))

# Decode a read-only buffer
import array
a = array.array('b', b'\x00\x00\x00\x0a')
print(st.unpack_from(a, 0))

# Decode an array
print(st.unpack_from(a, a.itemsize))

# Decode a buffer-like object
print(st.unpack_from(memoryview(a), a.itemsize*2))

# Try to decode a string
try:
    st.unpack(b'hello')
except Exception as e:
    print
