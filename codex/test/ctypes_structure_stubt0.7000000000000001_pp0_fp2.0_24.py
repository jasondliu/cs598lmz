import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(3)
    y = ctypes.c_int(4)
    z = ctypes.c_int(5)

s = S()
s.x = 100
s.y = 200
s.z = 300

