from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<hL')
s.pack(1,2)
s.size == s.size
s.format == s.format
################################################################################
# Test new Struct on many format strings
################################################################################
for f in ['B', 'L', '5H', '5l', '5f', '5d', '5b', '5B', '5H', '5h', '5b', '5B', '5x']:
    s = Struct.__new__(Struct)
    s.__init__(f)
    s.unpack(s.pack(*range(0, s.size))) == tuple(range(0, s.size))
################################################################################
# Tests from the module docstring
################################################################################
from _struct import Struct
st = Struct(">hL")
st.pack(1,2)
st.size == st.size
st.format == st.format
st.unpack( st.pack(1, 2) ) == (1,2)
################################################################################
# Test Struct on many format strings
################################################################################
