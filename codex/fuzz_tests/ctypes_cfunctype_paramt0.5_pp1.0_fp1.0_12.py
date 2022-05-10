import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print a, b
    return a+b

foo = FUNTYPE(callback)

lib.do_something(foo)
</code>

