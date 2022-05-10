import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def test_getattr():
    s = S()
    assert s.x == 0
    s.x = 42
    assert s.x == 42

def test_setattr_after_init():
    s = S()
    assert s.x == 0
    s.x = 42
    assert s.x == 42
    s = S(1)
    assert s.x == 1
    s.x = 42
    assert s.x == 42

def test_setattr_after_init_valueerror():
    s = S()
    raises(ValueError, "s.y = 1")
    raises(ValueError, "s.y = 1")
    s = S(1)
    raises(ValueError, "s.y = 1")
    raises(ValueError, "s.y = 1")

def test_delattr():
    s = S()
    assert s.x
