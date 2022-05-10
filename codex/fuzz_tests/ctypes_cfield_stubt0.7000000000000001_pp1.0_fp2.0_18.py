import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    pass
X._fields_ = [('x', ctypes.c_int)]

def test_cfield():
    assert isinstance(X.x, ctypes.CField)
    assert isinstance(S.x, ctypes.CField)
    #
    X_x = X.x
    S_x = S.x
    assert isinstance(X_x, ctypes.CField)
    assert isinstance(S_x, ctypes.CField)
    #
    assert isinstance(S.x.offset, int)
    assert isinstance(S.x.size, int)
    assert isinstance(S.x.bitsize, int)
    assert isinstance(S.x.name, str)
    assert isinstance(S.x.type, type)
    assert isinstance(S.x.ofs, int)
    assert isinstance(S.x.restype, type)
    assert isinstance(S.x.argtypes, tuple)
    assert isinstance(S.x.proto
