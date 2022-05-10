import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    s = S()
    s.x = 42
    assert s.x == 42
    assert S.x.__get__(s, S) == 42
    with pytest.raises(AttributeError):
        S.x.__set__(s, 43)
    with pytest.raises(AttributeError):
        del S.x
    with pytest.raises(AttributeError):
        S.x.__delete__(s)

def test_cfield_pointer():
    s = S()
    s.x = 42
    p = ctypes.pointer(s)
    assert p.contents.x == 42
    p.contents.x = 43
    assert s.x == 43
    p.contents.x += 1
    assert s.x == 44

def test_typeerror():
    s = S()
    with pytest.raises(TypeError):
        s.x = "string"
    with pytest.raises(TypeError):
        s.x = 42.0

def test
