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

def test_CField():
    p = POINT(2, 3)
    assert p.x == 2
    assert p.y == 3
    p.x = 4
    assert p.x == 4
    assert p.y == 3
    p.y = 5
    assert p.x == 4
    assert p.y == 5
    r = RECT(1, 2, 3, 4)
    assert r.left == 1
    assert r.top == 2
    assert r.right == 3
    assert r.bottom == 4
    r.left = 5
    assert r.left == 5
    assert r.top == 2
