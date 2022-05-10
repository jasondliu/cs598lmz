import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print(x + y)
    return x + y

my_callback = FUNTYPE(my_callback)

lib.my_func(my_callback)
</code>

