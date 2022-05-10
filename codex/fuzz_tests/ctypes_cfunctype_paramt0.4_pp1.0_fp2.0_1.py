import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(arg1, arg2):
    print "my_callback called with %d, %d" % (arg1, arg2)
    return 0

lib = ctypes.CDLL("libmylib.so")
lib.register_callback.argtypes = [FUNTYPE]
lib.register_callback.restype = None
lib.call_callback(2, 3)
lib.register_callback(FUNTYPE(my_callback))
lib.call_callback(2, 3)
</code>

