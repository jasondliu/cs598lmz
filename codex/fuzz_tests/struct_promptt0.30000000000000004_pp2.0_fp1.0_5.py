import _struct
# Test _struct.Struct.__getitem__

def test_getitem():
    s = _struct.Struct('i')
    assert s[0] == 'i'
    raises(IndexError, s.__getitem__, 1)

def test_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    raises(TypeError, s.unpack, 1)
    raises(TypeError, s.unpack, 'a')
    raises(TypeError, s.unpack, b'a')
    raises(TypeError, s.unpack, b'\x01\x00\x00\x00\x00')
    raises(TypeError, s.unpack, b'\x01\x00\x00')
    raises(TypeError, s.unpack, b'\x01\x00\x00\x00\x00')
    raises(TypeError, s.unpack, b'\x01\x00\x00')

def test_pack
