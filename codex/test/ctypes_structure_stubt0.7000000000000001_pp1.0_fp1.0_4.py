import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
print(s.x)
s.x = 3
print(s.x)

s.x = ctypes.c_int(s.x)
print(s.x)
s.x = ctypes.c_int(3)
print(s.x)
