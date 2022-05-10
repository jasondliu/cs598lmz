import ctypes
# Test ctypes.CFUNCTYPE

#
# so, first, the results with the standard ctypes CFUNCTYPE stuff,
# just to see what type is returned.
#

# this should return "int (*)(unsigned char *, int)"
print ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte),
                       ctypes.c_int)

# this should return "int (*)(const unsigned char *, int)"
print ctypes.CFUNCTYPE(ctypes.c_int,
                       ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)

# this should return "int (*)(const unsigned char *, const int)"
print ctypes.CFUNCTYPE(ctypes.c_int,
                       ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)

#
# okay, now, actually create one of these types
#

# this should return "int (*)(unsigned char *, int)"
c_func = ctypes.CFUN
