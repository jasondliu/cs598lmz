import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print(x + y)
    return x + y

cb_func = FUNTYPE(my_callback)
</code>

