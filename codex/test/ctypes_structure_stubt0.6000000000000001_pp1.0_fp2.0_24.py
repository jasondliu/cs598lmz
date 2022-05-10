import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong

a = S()
a.x = 2**31
print(a.x)
