import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print a, b
    return a + b

lib = ctypes.CDLL('./libtest.so')
lib.func.argtypes = [ctypes.c_int, ctypes.c_int]
lib.func.restype = ctypes.c_int

lib.func(1, 2)

lib.func_callback.argtypes = [FUNTYPE]
lib.func_callback(FUNTYPE(func))
</code>

