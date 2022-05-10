import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("Callback called with %d" % x)
    return 0

my_callback_func = FUNTYPE(my_callback)

# Callback is called from C code.
my_callback_func(42)

# Callback is called from Python code.
my_callback_func(42)
</code>

