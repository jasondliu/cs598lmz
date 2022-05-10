import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 2

def f(): return 1, [1]

s = S()
