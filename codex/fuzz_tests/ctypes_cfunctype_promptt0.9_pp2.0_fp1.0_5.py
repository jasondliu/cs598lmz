import ctypes
# Test ctypes.CFUNCTYPE by calling the set_error_handler function in Xlib.
prototype = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
C_set_error_handler = prototype(('XSetErrorHandler', cdll),
                                ((1,), (1,)))
print "%d" % C_set_error_handler(0)
