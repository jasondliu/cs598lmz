import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.__dict__)
s.x = 1
s.y = 2
print(s.__dict__)
