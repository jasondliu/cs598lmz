import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print(i)
    return i

my_callback_c = FUNTYPE(my_callback)

lib.call_function(my_callback_c)
</code>

