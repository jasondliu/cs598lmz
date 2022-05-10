import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print("my_callback", x, y)
    return x + y

my_callback_c = FUNTYPE(my_callback)

my_callback_c(1, 2)
</code>

