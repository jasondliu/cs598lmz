import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

s = S()
s.x = 1
s.y = 2.0

print(s.x, s.y)

#s = S(x=1, y=2.0)
#s = S(1, 2.0)
#s = S(y=2.0, x=1)
#s = S(y=2.0, 1)
#s = S(1, y=2.0)
#s = S(2.0, 1)
#s = S(2.0, x=1)
#s = S(x=1, 2.0)
#s = S(2.0, x=1)
#s = S(x=1, 2.0)
#s = S(y=2.0, x=1)
#s = S(y=2.0, x=1)
#s = S(y=2.0, x=1)
#s = S(y=2.0, x=1)
#
