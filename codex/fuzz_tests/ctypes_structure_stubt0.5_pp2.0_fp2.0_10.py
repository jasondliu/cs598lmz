import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def test_pass_struct():
    def f(s):
        return s.x + s.y + s.z
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    assert f(s) == 6

def test_pass_struct_by_value():
    def f(s):
        return s.x + s.y + s.z
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    assert f(s) == 6

def test_pass_struct_by_ref():
    def f(s):
        return s.x + s.y + s.z
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    assert f(s) == 6

def test_pass_struct_by_ptr():
    def f(s):
        return
