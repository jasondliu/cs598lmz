import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    i = ctypes.c_int()
    f1 = ctypes.c_float()
    f2 = ctypes.c_float()

#s = S(i=3) # TypeError: Type S takes no arguments
s = S()
s.i = 3
