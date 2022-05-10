import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print("callback called with", i)
    return i * 2

CALLBACK = FUNTYPE(my_callback)

lib.my_function(1, CALLBACK)
</code>

