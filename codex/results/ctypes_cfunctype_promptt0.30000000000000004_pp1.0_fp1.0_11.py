import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x, y):
    return x + y

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cfunc = CFunc(func)

print cfunc(1, 2)

print cfunc.__name__

print cfunc.__doc__

print cfunc.__module__

print cfunc.__dict__

print cfunc.__class__

print cfunc.__closure__

print cfunc.__code__

print cfunc.__defaults__

print cfunc.__globals__

print cfunc.__name__

print cfunc.__dict__

print cfunc.__self__

print cfunc.__call__(1, 2)

print cfunc.__get__(1, 2)
