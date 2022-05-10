import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "callback called with", a, b
    return a + b

# Convert the Python callback into a C callback
cb = FUNTYPE(my_callback)

# Call the C function, which will in turn call the Python callback
lib.call_callback(cb, 1, 2)
</code>

