import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_float),
                ('y', ctypes.c_float)]

s1 = S()
s1.x = 4.6
s1.y = 3.2
