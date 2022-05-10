import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

class D(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

def f(s):
    s.x = 1.0
    s.y = 2.0
    s.z = 3.0

def g(d):
    d.x = 1.0
    d.y = 2.0
    d.z = 3.0

s = S()
d = D()

f(s)
g(d)

