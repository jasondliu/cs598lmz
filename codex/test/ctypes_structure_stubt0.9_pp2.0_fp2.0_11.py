import ctypes

class S(ctypes.Structure):
    x = 23
    _fields_ = [('a', ctypes.c_int32),
                ('b', ctypes.c_int32),
                ('c', (ctypes.c_int32 * 2))]

def test():
    s = S(1, 2, (3, 4))
