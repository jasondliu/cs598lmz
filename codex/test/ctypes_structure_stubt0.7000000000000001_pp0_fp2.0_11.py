import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint
    y = ctypes.c_uint

def f(a, b):
    if a.contents.x == b.contents.x:
        print('equals!')

s1 = S()
s1.x = 1
s1.y = 2
