import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print 'got', a, b
    return a + b

CALLBACK = FUNTYPE(my_callback)

lib.my_callback.argtypes = (ctypes.c_int, ctypes.c_int)
lib.my_callback.restype = ctypes.c_int

lib.my_callback(1, 2)
# got 1 2
# 3
</code>

