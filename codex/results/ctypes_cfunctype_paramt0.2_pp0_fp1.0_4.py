import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

func_ptr = FUNTYPE(func)
print(func_ptr(1))
</code>

