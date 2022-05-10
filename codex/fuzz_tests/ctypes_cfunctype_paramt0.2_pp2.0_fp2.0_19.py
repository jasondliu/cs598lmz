import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

c_callback = FUNTYPE(my_callback)

# Callback type as a function prototype
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

c_callback = my_callback

# Callback type as a function prototype with restype and argtypes
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

my_callback.rest
