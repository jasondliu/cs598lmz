import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32
    _fields_ = [('x', ctypes.c_uint32),
                ('y', ctypes.c_uint32)]

def _test(x, y, use_fields=True):
    if use_fields:
        s = S()
        s.x = x
        s.y = y
        z = s.x + s.y
        return z

