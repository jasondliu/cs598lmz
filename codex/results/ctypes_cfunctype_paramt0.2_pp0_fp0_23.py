import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback called with %d" % x)
    return x + 1

# Convert the Python function into C callback
c_callback = FUNTYPE(my_callback)

# Call the C function, which will in turn call the Python callback
lib.call_callback(c_callback)
</code>

