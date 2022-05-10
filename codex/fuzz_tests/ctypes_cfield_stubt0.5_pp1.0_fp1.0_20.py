import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField():
    assert repr(S.x) == "<CField 'x' of 'S' objects>"
    assert S.x.__doc__ == "C integer field"
    assert S.x.__objclass__ is S
    assert S.x.__name__ == "x"
    assert S.x.__offset__ == 0
    assert S.x.__type__ == ctypes.c_int
    assert S.x.__size__ == ctypes.sizeof(ctypes.c_int)
    assert S.x.__index__ == 0

def test_CField_in_class():
    class C(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]

    assert repr(C.x) == "<CField 'x' of 'C' objects>"
    assert C.x.__doc__ == "C integer field"
    assert C.x.__objclass__ is C
    assert C.x.__name__ == "x"
    assert C.x.__offset__ == 0
