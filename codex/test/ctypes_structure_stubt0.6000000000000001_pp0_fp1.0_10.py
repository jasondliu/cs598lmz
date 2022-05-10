import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

def f(a):
    a.contents.x = 1
    a.contents.y = 2
    return a

s = S()
s_p = ctypes.pointer(s)
s_p = f(s_p)
