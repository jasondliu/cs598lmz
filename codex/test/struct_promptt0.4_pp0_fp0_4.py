import _struct
# Test _struct.Struct

def test_Struct():
    st = _struct.Struct('i')
    assert st.size == _struct.calcsize('i')
    assert st.pack(1) == _struct.pack('i', 1)
    assert st.unpack(st.pack(1)) == (1,)
    assert st.unpack_from(st.pack(1), 0) == (1,)
    assert st.unpack_from(st.pack(1) + st.pack(2), 0) == (1,)
    assert st.unpack_from(st.pack(1) + st.pack(2), st.size) == (2,)
    assert st.unpack_from(st.pack(1) + st.pack(2), st.size, 1) == (2,)
    raises(struct.error, st.unpack_from, st.pack(1) + st.pack(2), 2*st.size)
    raises(struct.error, st.unpack_from, st.pack(1) + st.pack(2), 2*st.size, 1)
