import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_class():
    assert isinstance(S.x, ctypes.CField)
    assert issubclass(ctypes.CField, ctypes.Field)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert ctypes.CField is ctypes.c_int

def test_cfield_instance():
    assert isinstance(S().x, ctypes.CField)
    assert isinstance(S().x, ctypes.c_int)

def test_cfield_repr():
    assert repr(S.x) == "<CField 'x' of type 'c_int'>"

def test_cfield_get_set():
    s = S()
    s.x = 42
    assert s.x == 42

def test_cfield_set_fail():
    s = S()
    try:
        s.x = 'foo'
    except TypeError:
        pass
    else:
        assert False

def test_cfield_get_fail():
    s = S
