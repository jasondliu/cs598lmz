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
    p = POINT(1,2)
    assert p.x == 1
    assert p.y == 2
    p.x = 3
    assert p.x == 3
    assert p.y == 2
    p.y = 4
    assert p.x == 3
    assert p.y == 4
    p = POINT(x=5, y=6)
    assert p.x == 5
    assert p
