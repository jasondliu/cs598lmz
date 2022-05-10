import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(0)
    y = ctypes.c_float(0)

s = S()
s.x = 0.5
s.y = 1.5
print(s.x, s.y)

s = S(x=0.5, y=1.5)
print(s.x, s.y)

