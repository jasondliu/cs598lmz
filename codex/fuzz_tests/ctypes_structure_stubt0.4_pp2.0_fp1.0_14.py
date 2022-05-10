import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def f(x):
    return x + 1

def g(x):
    return x + 2

def h(x):
    return x + 3

def f_ptr(x):
    return f(x)

def g_ptr(x):
    return g(x)

def h_ptr(x):
    return h(x)

def test_simple():
    s = S(1, 2, 3)
    assert s.x == 1
    assert s.y == 2
    assert s.z == 3

def test_simple_ptr():
    s = S(1, 2, 3)
    assert s.x == 1
    assert s.y == 2
    assert s.z == 3
    assert f_ptr(s.x) == 2
    assert g_
