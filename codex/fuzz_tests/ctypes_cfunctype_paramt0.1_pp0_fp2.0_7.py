import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with", x)
    return x

cb = FUNTYPE(my_callback)

# now call the function
lib.my_function(cb)
</code>

