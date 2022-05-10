import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(arg):
    print 'called back with', arg
    return 0

CALLBACK = FUNTYPE(my_callback)

# Now 'CALLBACK' can be passed as argument to C functions that take
# a function pointer as argument.

# When the callback is called from C, the ctypes pythonapi is used to
# convert the arguments to python objects and then the python callback
# is called.

# The callback is called from a separate thread.

# To prevent the python interpreter from being shutdown while the
# callback is running, you must hold a reference to the CALLBACK object
# somewhere.

# The callback can be a global function, a class method or any other
# callable python object.  The only restriction is that the callback
# must be able to be called from a separate thread.

# The callback must return an integer value.

# The callback can be called with one integer argument.

# The callback can also be called with no arguments.  In this case, the
# argument to the callback is set to
