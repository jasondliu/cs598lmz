import ctypes

class S(ctypes.Structure):
    x = 1

def f(y):
    return y.x

f(S())
