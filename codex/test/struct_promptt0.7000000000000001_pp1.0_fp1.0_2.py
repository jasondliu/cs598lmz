import _struct
# Test _struct.Struct

def test_struct_simple():
    st = _struct.Struct('i')
    assert st.size == 4
    assert st.pack(0x12345678) == b'\x78\x56\x34\x12'
    assert st.unpack(b'\x78\x56\x34\x12') == (0x12345678,)

    assert st.pack_into(bytearray(8), 0, 0x12345678) == 8
    assert st.unpack_from(b'\x12\x34\x56\x78', 0) == (0x12345678,)
    assert st.unpack_from(bytearray(b'\x12\x34\x56\x78'), 0) == (0x12345678,)
    assert st.unpack_from(bytearray(b'\x12\x34\x56\x78'), 1) == (0x345678,)
