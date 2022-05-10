import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(x, y):
    return x+y

fptr = FUNTYPE(func)

print(fptr(2,3))
</code>

