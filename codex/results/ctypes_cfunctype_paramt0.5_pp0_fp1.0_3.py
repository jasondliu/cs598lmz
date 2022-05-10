import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

cfunc = FUNTYPE(f)
cfunc(2)

# Type checking
def f(x):
    return x**2

cfunc = FUNTYPE(f)
cfunc('hi')

# Type casting
def f(x):
    return x**2

cfunc = FUNTYPE(f)
cfunc(2.0)
cfunc(2)
cfunc(2.0)

# Pointers
p = ctypes.pointer(ctypes.c_double(41.0))
print(p)
print(p.contents)

# Array
a = ctypes.c_double * 3
print(a)

# Structures
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

p = Point(1, 2)
p.x
p.y
p.x = 3.14
p.y =
