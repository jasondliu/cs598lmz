import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("Callback called with %d" % x)
    return 0

# Convert the Python callback into C callback
c_callback = FUNTYPE(my_callback)

# Call the C function, which will call the Python callback
lib.call_callback(c_callback)
</code>

