import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)

S1 = S()
S2 = S()

S1.x = 1
S1.y = 2
S2.x = 3
S2.y = 4

