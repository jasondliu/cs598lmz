import ctypes
# Test ctypes.CField

def test_CField():
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_uint8),
                    ("b", ctypes.c_uint8, 4),
                    ("c", ctypes.c_uint8, 4)]

    x = X(1, 2, 3)
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3
    assert x.a == 1

