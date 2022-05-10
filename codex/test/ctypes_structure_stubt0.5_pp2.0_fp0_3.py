import ctypes

class S(ctypes.Structure):
    x = ctypes.c_bool
    y = ctypes.c_bool
    _fields_ = [('x', ctypes.c_bool), ('y', ctypes.c_bool)]

s = S()
