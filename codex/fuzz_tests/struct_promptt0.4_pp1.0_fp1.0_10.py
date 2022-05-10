import _struct
# Test _struct.Struct.format_size() and _struct.Struct.size.
st = _struct.Struct('h')
assert st.format_size() == 2
assert st.size == 2
# Test _struct.Struct.__new__()
st = _struct.Struct('h')
assert st.format == 'h'
assert st.size == 2
assert st.format_size() == 2
# Test _struct.Struct.pack()
st = _struct.Struct('h')
assert st.pack(1) == b'\x01\x00'
assert st.pack(-1) == b'\xff\xff'
assert st.pack(2**15-1) == b'\xff\x7f'
assert st.pack(-2**15) == b'\x00\x80'
assert st.pack(2**15) == b'\x00\x80'
assert st.pack(-2**15-1) == b'\xff\x7f'
assert st.pack(2**16-1) == b'\xff\xff'
assert st.pack(-2**16)
