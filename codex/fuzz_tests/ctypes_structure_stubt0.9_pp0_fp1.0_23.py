import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_short
    z = ctypes.c_char

s = S()
print(ctypes.sizeof(S))
print(ctypes.sizeof(s))
print(ctypes.sizeof(S) == ctypes.sizeof(s))
