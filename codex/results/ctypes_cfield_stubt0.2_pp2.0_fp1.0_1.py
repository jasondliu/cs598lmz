import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert isinstance(S.x, ctypes.Field)
    assert not isinstance(S.x, ctypes.Array)
    assert not isinstance(S.x, ctypes.Pointer)
    assert not isinstance(S.x, ctypes.Union)
    assert not isinstance(S.x, ctypes.Structure)
    assert not isinstance(S.x, ctypes.CFuncPtr)
    assert not isinstance(S.x, ctypes.CArray)
    assert not isinstance(S.x, ctypes.PYFUNCTYPE)
    assert not isinstance(S.x, ctypes.CData)
    assert not isinstance(S.x, ctypes.CDataMeta)
    assert not isinstance(S.x, ctypes.CDataMeta)
    assert not isinstance(S.x, ctypes.CDataMeta)
    assert not isinstance(S.x, ctypes.CDataMeta)
    assert not is
