import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print("my_callback called with %d, %d" % (x, y))
    return x + y

my_callback_c = FUNTYPE(my_callback)

lib.my_function.argtypes = (ctypes.c_int, ctypes.c_int, FUNTYPE)
lib.my_function(1, 2, my_callback_c)
</code>

