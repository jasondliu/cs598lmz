import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with", x)
    return x + 1

cb = FUNTYPE(my_callback)

# now cb is a ctypes callback object

# now call the callback
cb(42)

# you can also pass cb to a C function that takes a function pointer
# as an argument

# define a C function that takes a function pointer as an argument
# and calls it
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, FUNTYPE)

def call_my_callback(cb):
    return cb(42)

call_my_callback(cb)
</code>

