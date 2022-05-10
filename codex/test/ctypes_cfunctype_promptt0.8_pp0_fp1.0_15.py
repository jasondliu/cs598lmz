import ctypes
# Test ctypes.CFUNCTYPE

#
# so, first, the results with the standard ctypes CFUNCTYPE stuff,
# just to see what type is returned.
#

# this should return "int (*)(unsigned char *, int)"
