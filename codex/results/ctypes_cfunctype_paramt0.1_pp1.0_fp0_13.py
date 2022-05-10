import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with", x)
    return x + 1

my_callback_c = FUNTYPE(my_callback)

lib.register_callback(my_callback_c)

lib.call_callback(42)
</code>

