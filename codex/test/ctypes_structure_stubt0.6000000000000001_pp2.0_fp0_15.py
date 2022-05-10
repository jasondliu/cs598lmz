import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)


s = S()

s.x = 1
print(s.x)

s.x = 2
print(s.x)
