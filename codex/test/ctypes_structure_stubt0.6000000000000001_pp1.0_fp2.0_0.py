import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_float()

class S2(ctypes.Structure):
    _fields_ = (('x', ctypes.c_int),
                ('y', ctypes.c_float))

#s = S()
#s.x = 42
#s.y = 3.14

