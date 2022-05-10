import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("Callback called with %d and %d" % (a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

dll.set_callback(my_callback_c)

dll.call_callback(1, 2)
</code>

