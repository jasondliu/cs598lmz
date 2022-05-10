import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    _fields_ = [
            ("x", ctypes.c_double),
            ("y", ctypes.c_double),
            ("z", ctypes.c_double),
            ("w", ctypes.c_double),
            ]

v = S()
v.x = 1.0
v.y = 2.0
v.z = 3.0
v.w = 4.0

print v

raw_input()
