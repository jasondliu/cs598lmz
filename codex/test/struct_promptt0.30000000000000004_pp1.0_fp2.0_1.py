import _struct
# Test _struct.Struct.__new__

class S(object):
    def __new__(cls, *args):
        return _struct.Struct(*args)

def test_new():
    s = S('i')
    assert s.size == 4

# Test _struct.Struct.__getitem__

def test_getitem():
    s = _struct.Struct('i')
    assert s[0] == 'i'
    raises(IndexError, s.__getitem__, 1)

# Test _struct.Struct.__setitem__

def test_setitem():
    s = _struct.Struct('i')
    raises(TypeError, s.__setitem__, 0, 'i')

# Test _struct.Struct.__len__

def test_len():
    s = _struct.Struct('i')
    assert len(s) == 1

# Test _struct.Struct.__repr__

def test_repr():
    s = _struct.Struct('i')
    assert repr(s) == "Struct('i')"

# Test
