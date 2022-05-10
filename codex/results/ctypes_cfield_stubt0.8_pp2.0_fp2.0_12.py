import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

class Y(ctypes.c_int):
    pass

class Z(X):
    pass

def test_member_class_and_pointer():
    a = S()
    p = ctypes.pointer(a)
    ctypes.CFieldPointer = type(p.contents.x)
    assert issubclass(X, ctypes.CField)
    assert issubclass(Y, ctypes.CField)
    assert issubclass(Z, ctypes.CField)
    assert issubclass(ctypes.CField, ctypes.CFieldPointer)
