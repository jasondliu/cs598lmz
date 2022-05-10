import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print f_c(2)

#------------------------------------------------------------------------------

import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

def f(x):
    return x**2

f_c = ctypes.CFUNCTYPE(ctypes.c_double, Point)(f)

print f_c(Point(2,3))

#------------------------------------------------------------------------------

import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

def f(x):
    return x**2

f_c = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(Point))(f)

print f_c(Point(2,3))

