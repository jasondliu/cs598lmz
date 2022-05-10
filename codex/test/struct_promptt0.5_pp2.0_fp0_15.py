import _struct
# Test _struct.Struct.__getitem__

def test_getitem():
    s = _struct.Struct('i')
    assert s[0] == 'i'

def test_getitem_fail():
    s = _struct.Struct('i')
    raises(TypeError, s.__getitem__)
    raises(TypeError, s.__getitem__, 0, 1)
    raises(IndexError, s.__getitem__, 1)

def test_getitem_fail_unpack():
    s = _struct.Struct('i')
    raises(TypeError, s.__getitem__, 'ABC')

def test_getitem_fail_pack():
    s = _struct.Struct('i')
    raises(TypeError, s.__getitem__, 1, 2)

def test_getitem_unpack():
    s = _struct.Struct('i')
    assert s[0, b'\x00\x00\x00\x00'] == (0,)

def test_getitem_pack():
    s = _struct.Struct('i')

