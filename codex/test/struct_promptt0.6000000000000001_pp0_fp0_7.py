import _struct
# Test _struct.Struct.__doc__
# Test _struct.Struct.format
def test_format():
    for fmt, size in (('i', 4), ('l', 4), ('f', 4), ('d', 8), ('P', 8)):
        st = _struct.Struct(fmt)
        assert st.format == fmt
        assert st.size == size
        assert st().format == fmt
        assert st().size == size
        assert _struct.Struct(st).format == fmt
        assert _struct.Struct(st).size == size
        assert _struct.Struct(st()).format == fmt
        assert _struct.Struct(st()).size == size
def test_pack():
    st = _struct.Struct('i')
    assert st.pack(42) == b'*\x00\x00\x00'
    assert st.pack(42).decode('ascii') == '*\x00\x00\x00'
    raises(struct.error, st.pack)
    raises(struct.error, st.pack, 'foo')
