import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_callback():
    cb = FUNTYPE(lambda x: x+1)
    assert cb(41) == 42

def test_callback_with_struct():
    class S(ctypes.Structure):
        _fields_ = [('a', ctypes.c_int),
                    ('b', ctypes.c_int)]
    cb = FUNTYPE(lambda x: x+1)
    s = S(1, 2)
    assert cb(s.a) == 2
    assert cb(s.b) == 3
