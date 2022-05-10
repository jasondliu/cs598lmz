import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(x, y):
    return x + y

f_c = FUNTYPE(f)
f_c(1, 2)

#%%
import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

def p_distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

p_distance_c = ctypes.CFUNCTYPE(ctypes.c_double, Point, Point)(p_distance)

p1 = Point(1, 2)
p2 = Point(4, 5)
p_distance_c(p1, p2)

#%%
# 将函数转换为C函数对象
import ctypes

def f
