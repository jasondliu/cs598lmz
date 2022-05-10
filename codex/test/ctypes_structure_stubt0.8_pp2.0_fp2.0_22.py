import ctypes

class S(ctypes.Structure):
    x = 0
    y = 0
    z = ctypes.c_float(1.0)
    
class C(ctypes.Structure):
    _pack_ = 1
    _fields_ = ('a', ctypes.c_short), ('b', ctypes.c_int)

def test_size():
    assert sizeof(ctypes.c_char) == 1
    assert sizeof(ctypes.c_short) == 2
    assert sizeof(ctypes.c_int) == 4
    assert sizeof(ctypes.c_long) == 4
    assert sizeof(ctypes.c_longlong) == 8
    if ctypes.sizeof(ctypes.c_void_p) == 4:
        assert sizeof(ctypes.c_size_t) == 4
    else:
        assert sizeof(ctypes.c_size_t) == 8
    #
    assert sizeof(ctypes.c_float) == 4
    assert sizeof(ctypes.c_double) == 8
    assert sizeof(ctypes.c_longdouble) == 8
    #
