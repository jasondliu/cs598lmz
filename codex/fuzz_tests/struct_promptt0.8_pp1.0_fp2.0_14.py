import _struct
# Test _struct.Struct.get_size() and _struct.Struct.format_size()
# with aligned data
st = _struct.Struct('<i')
assert st.format_size() == st.get_size()
st = _struct.Struct('<ii')
assert st.format_size() == st.get_size()
# Test _struct.Struct.get_size() and _struct.Struct.format_size()
# with unaligned data
st = _struct.Struct('<Q')
assert st.format_size() == st.get_size()
st = _struct.Struct('<QQ')
assert st.format_size() == st.get_size()
# Test _struct.Struct.get_size() and _struct.Struct.format_size()
# with unaligned data and alignment
st = _struct.Struct('<Q', 8)
assert st.format_size() == st.get_size()
st = _struct.Struct('<QQ', 8)
assert st.format_size() == st.get_size()
