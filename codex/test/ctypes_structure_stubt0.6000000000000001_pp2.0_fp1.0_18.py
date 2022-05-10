import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Union):
    _fields_ = [("s1", S),
                ("s2", S)]

def f(s):
    s.s1.x = 1
    s.s1.y = 2
    s.s2.x = 3
    s.s2.y = 4
    return s.s2.y

def main():
    t = T()
    t.s1.x = 0
    t.s1.y = 0
    assert f(t) == 4
    assert t.s1.x == 3
    assert t.s1.y == 4

