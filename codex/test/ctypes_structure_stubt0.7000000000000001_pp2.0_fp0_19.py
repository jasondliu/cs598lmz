import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def g(x):
    return S(x)

def run(expected):
    for i in range(5):
        s = g(15)
        assert s.x == expected

