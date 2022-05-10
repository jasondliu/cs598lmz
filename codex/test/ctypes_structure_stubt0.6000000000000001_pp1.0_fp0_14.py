import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(3)

s = S()

print(s.x)
print(ctypes.sizeof(s))
print(ctypes.sizeof(s.x))
