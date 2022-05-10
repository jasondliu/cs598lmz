import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 5
s.y = 6

print(s.x)
print(s.y)

print(s.__dict__)
