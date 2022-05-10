import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_get_cfield():
    from _ctypes import get_cfield
    assert get_cfield(S, 'x') is S.x

def test_get_cfield_missing():
    from _ctypes import get_cfield
    with raises(KeyError):
        get_cfield(S, 'y')

def test_get_cfield_non_cfield():
    from _ctypes import get_cfield
    assert get_cfield(S, '_fields_') is S._fields_

def test_get_cfield_obj2():
    from _ctypes import get_cfield
    assert get_cfield(S._fields_[0], 'name') is 'x'
