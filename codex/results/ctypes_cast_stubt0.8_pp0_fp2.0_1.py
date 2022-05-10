import ctypes
ctypes.cast(a,ctypes.c_void_p)

# ctypes example
# import ctypes
# from numpy.ctypeslib import ndpointer

# c_double_p = ctypes.POINTER(ctypes.c_double)

# _F4_f4_f4_p = ctypes.CDLL('f4_f4_f4.so').F4_f4_f4
# _F4_f4_f4_p.argtypes = [
#    ctypes.c_int32,
#    ctypes.c_int32,
#    ctypes.c_int32,
#    ctypes.c_int32,
#    ctypes.c_int32,
#    ctypes.c_double,
#    ctypes.c_double,
#    c_double_p,
#    c_double_p,
#    c_double_p,
#    c_double_p,
#    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
#    ndpointer
