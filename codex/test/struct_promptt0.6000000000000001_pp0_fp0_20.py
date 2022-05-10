import _struct
# Test _struct.Struct class
import struct

from test import test_support

# Example of packing and unpacking short and long integers.
st = _struct.Struct("hhl")
packed = st.pack(1, 2, 3)
