import ctypes
# Test ctypes.CFUNCTYPE by calling the set_error_handler function in Xlib.
prototype = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
