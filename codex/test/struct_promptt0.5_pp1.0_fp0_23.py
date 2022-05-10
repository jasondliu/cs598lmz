import _struct
# Test _struct.Struct

def test_struct_short():
    st = _struct.Struct('h')
    assert st.size == 2
    assert st.pack(0) == b'\0\0'
    assert st.pack(1) == b'\0\1'
    assert st.pack(-1) == b'\xff\xff'
    assert st.pack(0x1234) == b'\x12\x34'
    assert st.pack(-0x1234) == b'\xed\xcc'
    assert st.unpack(b'\0\0') == (0,)
    assert st.unpack(b'\0\1') == (1,)
    assert st.unpack(b'\xff\xff') == (-1,)
    assert st.unpack(b'\x12\x34') == (0x1234,)
    assert st.unpack(b'\xed\xcc') == (-0x1234,)

def test_struct_int():
    st = _struct.Struct('i')
    assert st.size == 4
