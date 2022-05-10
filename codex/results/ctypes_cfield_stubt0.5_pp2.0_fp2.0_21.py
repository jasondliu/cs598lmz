import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def _test(typ):
    assert isinstance(typ, ctypes.CField)
    assert isinstance(typ, ctypes.Field)
    assert isinstance(typ, ctypes._Pointer)
    assert not isinstance(typ, ctypes._SimpleCData)
    assert not isinstance(typ, ctypes._SimpleCData)
    assert not isinstance(typ, ctypes._Pointer)
    assert not isinstance(typ, ctypes._CData)
    assert not isinstance(typ, ctypes.Array)

_test(S.x)
_test(ctypes.c_int)
_test(ctypes.c_int())
