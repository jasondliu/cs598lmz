import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    z = ctypes.c_int(3)

s = S()
print(s.x, s.y, s.z)

s.x = ctypes.c_int(10)
print(s.x, s.y, s.z)

s.y = ctypes.c_int(20)
print(s.x, s.y, s.z)

s.z = ctypes.c_int(30)
print(s.x, s.y, s.z)
