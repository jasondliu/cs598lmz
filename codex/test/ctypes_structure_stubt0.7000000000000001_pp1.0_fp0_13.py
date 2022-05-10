import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 2

print(ctypes.sizeof(S))
print(ctypes.alignment(S))
s = S(x=0)
