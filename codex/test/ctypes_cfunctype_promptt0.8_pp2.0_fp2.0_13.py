import ctypes
# Test ctypes.CFUNCTYPE
# (e.g. see http://dirtsimple.org/2004/12/python-ctypes-tutorial.html)

int_p = ctypes.POINTER(ctypes.c_int)
#int_p = ctypes.c_void_p

# Callback function.
