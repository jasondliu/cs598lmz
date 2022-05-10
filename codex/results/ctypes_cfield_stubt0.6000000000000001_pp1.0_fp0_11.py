import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_get_c_field():
    assert get_c_field(S, 'x') is S.x

def test_get_c_field_not_found():
    with pytest.raises(AttributeError):
        get_c_field(S, 'y')
