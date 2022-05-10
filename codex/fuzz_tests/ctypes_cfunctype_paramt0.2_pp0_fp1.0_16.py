import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback = FUNTYPE(my_callback)

lib.my_function.argtypes = [FUNTYPE, ctypes.c_int, ctypes.c_int]
lib.my_function(my_callback, 1, 2)
</code>

