import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

def test_cfield():
    import sys
    if sys.maxsize > 2**32:
        ctypes.sizeof(ctypes.c_longlong) == 8
    else:
        ctypes.sizeof(ctypes.c_longlong) == 4

    assert ctypes.sizeof(ctypes.c_int) == 4
    assert ctypes.sizeof(ctypes.c_long) == 4
    assert ctypes.sizeof(ctypes.c_short) == 2
    assert ctypes.sizeof(ctypes.c_char) == 1
    assert ctypes.sizeof(ctypes.c_byte) == 1
    assert ctypes.sizeof(ctypes.c_ubyte) == 1
    assert ctypes.sizeof(ctypes.c_ushort) == 2
    assert ctypes.
