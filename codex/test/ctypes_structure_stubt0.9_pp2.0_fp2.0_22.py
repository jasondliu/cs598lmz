import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    p = ctypes.POINTER(x)

def check(l, test):
    for i in range(len(l)):
        assert l[i] == i
        assert test(i)

l = range(25)
