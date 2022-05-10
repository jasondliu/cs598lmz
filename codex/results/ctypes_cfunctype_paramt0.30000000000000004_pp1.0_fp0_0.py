import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback", a, b)
    return a + b

cb = FUNTYPE(my_callback)

lib.test_callback(cb)
</code>

