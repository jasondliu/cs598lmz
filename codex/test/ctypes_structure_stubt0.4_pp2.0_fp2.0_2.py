import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong
    z = ctypes.c_longlong
    w = ctypes.c_longlong

print(ctypes.sizeof(S))
print(ctypes.alignment(S))

s = S()
print(ctypes.addressof(s))
