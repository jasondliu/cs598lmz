import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_OverflowError():
    raises(OverflowError, ctypes.c_int, 123456789012345678901234567890)
    raises(OverflowError, ctypes.c_uint, -1)
    raises(OverflowError, ctypes.c_short, 1234567890123)
    raises(OverflowError, ctypes.c_ushort, -1)
    raises(OverflowError, ctypes.c_long, 123456789012345678901234567890)
    raises(OverflowError, ctypes.c_ulong, -1)
    raises(OverflowError, ctypes.c_longlong, 123456789012345678901234567890)
    raises(OverflowError, ctypes.c_ulonglong, -1)
    raises(OverflowError, ctypes.c_ssize_t, -1)
    raises(OverflowError, ctypes.c_size_t, -1)
    raises(OverflowError, ctypes.c_float, 123
