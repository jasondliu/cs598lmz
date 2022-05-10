import ctypes
# Test ctypes.CFUNCTYPE
# https://docs.python.org/2/library/ctypes.html#ctypes.CFUNCTYPE

import ctypes

# C prototype of the callback function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_callback(a, b):
    print "Python callback called with %d and %d" % (a, b)
    return a + b

# Convert the Python callback into C callback
c_callback = prototype(py_callback)

# Call a C function that uses the callback
lib = ctypes.CDLL('./libcallback.so')
lib.process(1, 2, c_callback)
