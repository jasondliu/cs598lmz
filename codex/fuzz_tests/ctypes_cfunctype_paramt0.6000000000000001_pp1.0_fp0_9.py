import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def sin(x):
    return math.sin(x)

sin_func = FUNTYPE(sin)
print sin_func(math.pi/2)
