import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print(a, b)
    return a * b

my_callback = FUNTYPE(my_callback)

lib.run(my_callback)
</code>

