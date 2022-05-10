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

class POINT_RECT(ctypes.Structure):
    _fields_ = [("pt", POINT),
                ("rc", RECT)]

def test_CField():
    pr = POINT_RECT()
    pr.pt.x = 1
    pr.pt.y = 2
    pr.rc.left = 3
    pr.rc.top = 4
    pr.rc.right = 5
    pr.rc.bottom = 6
    assert pr.pt.x == 1
    assert pr.pt.y == 2
    assert pr.rc.left == 3
    assert pr.rc.top == 4
    assert pr
