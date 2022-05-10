import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    y = ctypes.c_long(2)


s = S()
print(s.x)
print(s.y)
s.x = ctypes.c_long(3)
print(s.x)
print(s.y)
s.x = ctypes.c_long(4)
print(s.x)
print(s.y)
