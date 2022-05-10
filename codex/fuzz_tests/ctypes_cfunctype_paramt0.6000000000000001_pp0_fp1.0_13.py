import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print(n)

func_c = FUNTYPE(func)

func_c(1)
</code>

