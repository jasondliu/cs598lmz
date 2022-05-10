import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
_fun = FUNTYPE(f)

from math import pi
from ctypes import c_double

def find_root(a, b, eps=1e-10):
    if f(a) * f(b) > 0:
        raise ValueError('Function has the same signs at the endpoints')
    
    while True:
        m = (a + b)/2
        if f(m) == 0 or abs(a - b) < eps:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
            
print(find_root(0, pi/2), '=', pi/4)

%timeit find_root(0, pi/2)

def find_root_ctypes(a, b, eps=1e-10):
    if _fun(c_double(a)) * _fun(c_double(b)) > 0:
        raise ValueError('
