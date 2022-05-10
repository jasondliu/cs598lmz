import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(a):
    print("callback called with", a)
    return 0

my_callback = FUNTYPE(my_callback)

lib.set_callback(my_callback)

lib.call_callback(42)
</code>

