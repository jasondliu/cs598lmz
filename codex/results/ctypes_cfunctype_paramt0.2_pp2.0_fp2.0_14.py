import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

cfunc = FUNTYPE(func)

print cfunc(2)
</code>
This works fine, but I want to pass a function that takes more than one argument.
<code>def func(x, y):
    return x**2 + y**2

cfunc = FUNTYPE(func)
</code>
This doesn't work, because <code>FUNTYPE</code> only takes one argument.
Is there a way to do this?


A:

You can use <code>ctypes.c_void_p</code> to pass a pointer to a struct.
<code>import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_void_p)

def func(point):
    return point.x**2 + point
