import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)
    y = ctypes.c_double(2.0)

s = S()
print(s.x, s.y)

try:
    s.x = 1.0
except ValueError:
    print("ERROR")

s.x = ctypes.c_double(1.0)
print(s.x)
