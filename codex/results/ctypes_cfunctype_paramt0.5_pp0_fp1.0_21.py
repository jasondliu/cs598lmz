import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return 1.0/x

f_c = FUNTYPE(f)

print(f_c(1.0))

#%%

import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

distance_c = ctypes.CFUNCTYPE(ctypes.c_double, Point, Point)(distance)

p1 = Point(0, 0)
p2 = Point(1, 1)

print(distance_c(p1, p2))

#%%

import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]
