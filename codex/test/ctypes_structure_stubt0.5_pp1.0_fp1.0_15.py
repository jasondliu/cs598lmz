import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8()
    y = ctypes.c_uint8()
    z = ctypes.c_uint8()

s = S()
s.x = 3
s.y = 2
s.z = 1

print(s.x)
print(s.y)
print(s.z)

