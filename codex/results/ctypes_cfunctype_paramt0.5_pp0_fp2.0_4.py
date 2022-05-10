import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int,ctypes.c_int)
def callback(a,b):
    print a,b

fun = FUNTYPE(callback)

# now use fun as the callback function

# or pass fun to other libraries
</code>

