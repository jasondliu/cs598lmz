import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

class POINT_PTR(ctypes.POINTER(POINT)):
    pass

class RECT_PTR(ctypes.POINTER(RECT)):
    pass

def test_CField():
    assert POINT._fields_ == [("x", ctypes.c_int),
                              ("y", ctypes.c_int)]
    assert RECT._fields_ == [("left", ctypes.c_int),
                             ("top", ctypes.c_int),
                             ("right", ctypes.c_int),
                             ("bottom", ctypes.c_int)]
    assert POINT_PTR
