import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with", x)
    return x + 1

my_callback_func = FUNTYPE(my_callback)

lib.my_callback_func = my_callback_func

lib.my_callback_func(5)
</code>

