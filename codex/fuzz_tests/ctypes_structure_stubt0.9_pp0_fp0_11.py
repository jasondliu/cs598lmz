import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32(1)
    y = x
    _fields_ = [("x", ctypes.c_int32), ("y", ctypes.c_int32, y)]

def test_positional_args():
    s = S()
    assert s.x == 1
    assert s.y == 1

class S2(ctypes.Structure):
    x = ctypes.c_int32(1)
    y = x
    z = ctypes.c_int32(0)
    _fields_ = [("x", ctypes.c_int32),
                ("z", ctypes.c_int32, z),
                ("y", ctypes.c_int32, y)]

def test_positional_args_middle():
    s = S2()
    assert s.x == 1
    assert s.y == 1
    assert s.z == 0

def test_bitfields():
    class Point(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int, 2),
                    ("
