import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback", a, b)
    return a + b

my_callback_c = FUNTYPE(my_callback)

lib.my_callback(my_callback_c)
</code>

