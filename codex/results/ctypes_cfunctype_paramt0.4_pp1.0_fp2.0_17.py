import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("{} + {} = {}".format(a, b, a+b))
    return a+b

cb_fun = FUNTYPE(my_callback)

lib.my_callback(cb_fun)
</code>

