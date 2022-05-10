import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x):
    return x * x

def g(x):
    return x + x

def h(x):
    return x * 2

def test_map():
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    assert map(f, s) == S(x=1, y=4, z=9)
    assert map(g, s) == S(x=2, y=4, z=6)
    assert map(h, s) == S(x=2, y=4, z=6)

def test_map_multiple():
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    assert map(f, s, s) == S(x=1, y=16, z=81)
