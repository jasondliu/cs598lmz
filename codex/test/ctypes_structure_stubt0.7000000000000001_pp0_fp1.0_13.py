import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

a = S()
a.x = 1
a.y = 2

b = S()
b.x = 3
b.y = 4

c = S()
c.x = 5
c.y = 6

# This works
a = b = c = S()
