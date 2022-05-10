import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class V(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_char * 6),
        ("values", S * 4),
        ("gps", S),
    ]

def test_read(v):
    assert v.id == b"foobar"
    assert v.values[0].x == 0
    assert v.values[0].y == 1
    assert v.values[0].z == 2
    assert v.values[1].x == 0
    assert v.values[1].y == 1
    assert v.values[1].z == 2
    assert v.values[2].x == 0
    assert v.values[2].y == 1
    assert v.values[2].z == 2
    assert v.values[3].x == 0
    assert v.values[3].y == 1
    assert v.values[3].z == 2
    assert v.gps.x == 0

