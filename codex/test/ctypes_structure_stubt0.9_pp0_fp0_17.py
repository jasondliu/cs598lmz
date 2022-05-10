import ctypes

class S(ctypes.Structure):
    x = -1
    y = -2
    z = -3
    _fields_ = [('x', ctypes.c_long),
                ('f', ctypes.c_float)]


s = S()
