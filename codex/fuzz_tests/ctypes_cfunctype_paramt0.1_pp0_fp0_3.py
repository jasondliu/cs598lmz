import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

lib.set_callback(my_callback_c)

print("3 + 5 = %d" % lib.call_callback(3, 5))
</code>

