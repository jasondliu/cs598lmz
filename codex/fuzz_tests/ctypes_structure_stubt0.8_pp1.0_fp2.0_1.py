import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

def f(s):
    print s.x
    print s.y
    s.x = s.x + 1
    s.y = s.y + 1
    print s.x
    print s.y
    return s.x + s.y

s = S()
s.x = 1
s.y = 2
print f(s)
