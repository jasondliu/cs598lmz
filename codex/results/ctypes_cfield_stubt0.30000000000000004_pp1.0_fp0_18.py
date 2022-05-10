import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert issubclass(ctypes.CField, ctypes.Field)
    assert issubclass(ctypes.CField, ctypes.Array)
    assert issubclass(ctypes.CField, ctypes.Pointer)
    assert issubclass(ctypes.CField, ctypes.SimpleType)
    assert issubclass(ctypes.CField, ctypes._SimpleCData)
    assert issubclass(ctypes.CField, ctypes._Pointer)
    assert issubclass(ctypes.CField, ctypes._CData)
    assert issubclass(ctypes.CField, ctypes._CDataMeta)
    assert issubclass(ctypes.CField, ctypes._CDataMeta)
    assert issubclass(ctypes.CField, ctypes._CDataMeta)
    assert issubclass(ctypes.CField, ctypes._CDataMeta)
    assert issubclass(ctypes.CField, ctypes._CDataMeta)
    assert issubclass(ctypes.CField, c
