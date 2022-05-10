import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def my_callback(x):
    print x
    return x

c_callback = FUNTYPE(my_callback)

lib.foo(c_callback)
</code>

