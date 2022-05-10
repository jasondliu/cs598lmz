import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

func_ptr = FUNTYPE(func)

print(func_ptr(1, 2)) # 3
</code>

