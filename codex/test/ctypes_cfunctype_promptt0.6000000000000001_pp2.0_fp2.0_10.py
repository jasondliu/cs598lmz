import ctypes
# Test ctypes.CFUNCTYPE
# This is the prototype of the callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Test ctypes.POINTER(ctypes.c_int)
# This is the prototype of the callback
prototype2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# Test ctypes.POINTER(ctypes.c_int)
# This is the prototype of the callback
prototype3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

# Test ctypes.POINTER(ctypes.c_char)
# This is the prototype of the callback
prototype4 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_char))

# Test ctypes.POINTER(ctypes.c_char)
# This is the prototype of the callback
