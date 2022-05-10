import _struct
# Test _struct.Struct class
import struct

from test import test_support

# Example of packing and unpacking short and long integers.
st = _struct.Struct("hhl")
packed = st.pack(1, 2, 3)
print st.unpack(packed)

# Example of packing and unpacking doubles.
st = _struct.Struct("dd")
packed = st.pack(1.0, 2.0)
print st.unpack(packed)

# Example of packing and unpacking strings.
st = _struct.Struct("5s5s")
packed = st.pack("hello", "world")
print st.unpack(packed)

# Example of packing and unpacking characters.
st = _struct.Struct("ccc")
packed = st.pack("a", "b", "c")
print st.unpack(packed)

# Example of packing and unpacking byte arrays.
st = _struct.Struct("8s8s")
packed = st.pack("abcdefgh", "ijklmnop")
print st.unpack(packed)

# Example of packing and unpacking bytes
