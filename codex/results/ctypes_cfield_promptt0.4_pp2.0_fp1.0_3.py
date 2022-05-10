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
    p = POINT(1, 2)
    assert p.x == 1
    assert p.y == 2
    p.x = 3
    p.y = 4
    assert p.x == 3
    assert p.y == 4
    assert p.__dict__ == {'x': 3, 'y': 4}
    assert p._fields_ == [('x', ctypes.c_int), ('y', ctypes.c_int)]
    assert repr(p) == "<POINT(x=3, y=4)>"
    r = RECT(1, 2, 3, 4)

