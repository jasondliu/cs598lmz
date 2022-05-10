import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong()
    y = ctypes.c_longlong()

s = S()
s.x = 10
print(s.x, s.y)
s.y = 20
print(s.x, s.y)
print(s.x)
