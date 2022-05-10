import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class R(ctypes.Structure):
    _fields_ = [('_', ctypes.c_void_p),
                ('x', ctypes.c_int),
                ('y', ctypes.c_int)]

s = S(x = 1, y = 2)
r = R(x = 1, y = 2)

