import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# callback function
def my_callback(x):
    print("my_callback called with ", x)
    return 0

# convert function to CFUNCTYPE
c_callback = FUNTYPE(my_callback)

# call C function
lib.c_func(c_callback)
</code>

