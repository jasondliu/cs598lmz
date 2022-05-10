import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_subclass():
    class X(ctypes.CField):
        pass

    class Y(ctypes.Structure):
        _fields_ = [('x', X)]

    assert issubclass(X, ctypes.CField)
    assert issubclass(X, ctypes._SimpleCData)
    assert issubclass(Y, ctypes.Structure)
    assert issubclass(Y, ctypes.Union)
    assert issubclass(Y, ctypes._CData)
    assert issubclass(Y, ctypes._Pointer)
    assert not issubclass(Y, ctypes.Array)
    assert not issubclass(Y, ctypes.CFuncPtr)

def test_cfield_subclass_with_name():
    class X(ctypes.CField):
        _name = "X"

    class Y(ctypes.Structure):
        _fields_ = [('x', X)]

    assert issubclass(X, ctypes.CField)
    assert issubclass(X, c
