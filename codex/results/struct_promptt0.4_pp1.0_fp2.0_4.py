import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, "did not catch bad format"

def test_struct_pack():
    st = _struct.Struct('i')
    sz = st.size
    pack = st.pack
    for i in (-1, 0, 1, 127, 128, 255, 256, 32767, 32768, 65535, 65536):
        assert pack(i) == _struct.pack('i', i)
        assert len(pack(i)) == sz

def test_struct_unpack():
    st = _struct.Struct('i')
    unpack = st.unpack
    for i in (-1, 0, 1, 127, 128, 255, 256, 32767, 32768, 65535, 65536):
        assert unpack(st.pack(i)) == (i,)

def test_struct_iter_unpack():
    st = _struct.Struct('i')
    unpack = st.iter_un
