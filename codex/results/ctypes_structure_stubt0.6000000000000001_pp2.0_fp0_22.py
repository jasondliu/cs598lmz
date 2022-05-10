import ctypes

class S(ctypes.Structure):
    x = 0
    _fields_ = [('x', ctypes.c_uint),
                ('y', ctypes.c_uint),
                ('z', ctypes.c_uint),
                ]

s = S()

print s.x
