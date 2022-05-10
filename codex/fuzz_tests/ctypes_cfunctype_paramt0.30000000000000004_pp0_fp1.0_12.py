import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(x):
    print("py_func", x)
    return x

c_func = FUNTYPE(py_func)

c_func(5)
</code>

