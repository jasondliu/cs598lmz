import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_func(a, b):
    return a + b

func = FUNTYPE(py_func)

print(func(1, 2))
</code>

