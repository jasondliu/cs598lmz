import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong()
    y = ctypes.c_int()

s = S()
print(type(s.x))
print(type(s.y))

s2 = ctypes.c_longlong()
s3 = ctypes.c_int()
print(type(s2))
print(type(s3))
