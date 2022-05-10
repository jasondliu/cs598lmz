import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print "callback called with", i
    return i * 2

# Convert the Python callback into a C pointer with an argtype of c_int.
cb_fun = FUNTYPE(my_callback)

# Callback function is called without error.
print mylib.call_callback(42, cb_fun)
</code>

