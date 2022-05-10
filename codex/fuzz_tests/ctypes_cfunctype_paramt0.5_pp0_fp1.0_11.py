import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def my_callback(arg1, arg2):
    print("callback called with %d %d" % (arg1, arg2))
    return 0

my_callback = FUNTYPE(my_callback)

lib.my_function.argtypes = [FUNTYPE, ctypes.c_int]
lib.my_function.restype = ctypes.c_int

lib.my_function(my_callback, 1)
</code>

