import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

x = S()
y = S()

x.x, x.y = 1, 2
y.x, y.y = 3, 4

