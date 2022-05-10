import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    s = S()
    s.x = 42
    s.y = -42
    assert s.x == 42
    assert s.y == -42

def test_cfield_in_union():
    class U(ctypes.Union):
        _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    u = U()
    u.x = 42
    assert u.x == 42
    assert u.y == 42
    u.y = -42
    assert u.x == -42
    assert u.y == -42

def test_cfield_in_union_with_array():
    class U(ctypes.Union):
        _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int*4)]
    u = U()
    u.x = 42
    assert u.x == 42

