import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("Callback called with", x)
    return 0

cb = FUNTYPE(my_callback)

# Call the C function
lib.my_function(42, cb)
</code>

