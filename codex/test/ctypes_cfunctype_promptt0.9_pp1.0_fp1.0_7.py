import ctypes
# Test ctypes.CFUNCTYPE() prototype object
AddParams = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_char_p, ctypes.c_char_p)
# Test ctypes.CFUNCTYPE() prototype object
AddStrParams = ctypes.CFUNCTYPE(ctypes.c_uint,
    ctypes.c_char_p, ctypes.c_char_p)
# Call a Python function by address
