import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():

    class S2(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]

    assert isinstance(S2.x, ctypes.CField)
    assert isinstance(S2.x, ctypes.CFuncPtr)
    assert not isinstance(S2.x, ctypes.CData)
    assert not isinstance(S2.x, ctypes.Structure)
    assert not isinstance(S2.x, ctypes.Union)

def test_cfield_setattr():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    s = S()

    # assigning to a field works
    old_value = s.x
    s.x = new_value = old_value + 1
    assert s.x == new_value

    # assigning to a non-field raises TypeError
    raises(TypeError, "setattr(s, 'y', 1)")

    # assigning to a field from a different type raises
