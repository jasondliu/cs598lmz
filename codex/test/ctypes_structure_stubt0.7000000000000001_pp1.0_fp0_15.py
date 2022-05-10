import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char

class D(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char
    z = ctypes.c_char

print(ctypes.sizeof(S))
print(ctypes.sizeof(D))
