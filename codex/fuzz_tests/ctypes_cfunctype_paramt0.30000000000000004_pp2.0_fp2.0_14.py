import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_func(x, y):
    return x + y

c_func = FUNTYPE(py_func)

print(c_func(1, 2))
</code>
This works, but I'm not sure if this is the right way to do it.

