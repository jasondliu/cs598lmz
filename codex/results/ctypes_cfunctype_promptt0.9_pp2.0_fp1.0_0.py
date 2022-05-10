import ctypes
# Test ctypes.CFUNCTYPE()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

cdoublepp = ctypes.POINTER(ctypes.c_double)
cdoublepp = ctypes.POINTER(cdoublepp)

# The following is not allowed
# error: object with incompatible pointer layout
# foo = ctypes.CFUNCTYPE(ctypes.c_int, 
#                        ctypes.c_int, ctypes.c_int, cdoublepp)

foo = ctypes.CFUNCTYPE(ctyp
