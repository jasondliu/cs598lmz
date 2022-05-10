import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

def func(s):
    print s.x, s.y

s = S()
s.x = 1
s.y = 2
func(s)
