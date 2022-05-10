import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()

print(s.x)
print(s.y)

print(s.__dict__)

s.x = 3

print(s.x)
print(s.y)

print(s.__dict__)
