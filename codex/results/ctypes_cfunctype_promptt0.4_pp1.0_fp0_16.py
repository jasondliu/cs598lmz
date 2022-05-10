import ctypes
# Test ctypes.CFUNCTYPE()

# This is the prototype of the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# This is the function that will be called by the callback
def callback(a, b):
    print "Callback called with %d and %d" % (a, b)

# Create the callback
cb = CALLBACKFUNC(callback)

# Call the callback
cb(1, 2)
</code>

