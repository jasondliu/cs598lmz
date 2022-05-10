import ctypes
# Test ctypes.CFUNCTYPE definition
# (i.e. verify that this file is not broken)
CFUNCTYPE0 = ctypes.CFUNCTYPE(ctypes.c_int)
CFUNCTYPE1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
CFUNCTYPE2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
CFUNCTYPE3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                             ctypes.c_int)
CFUNCTYPE4 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                             ctypes.c_int, ctypes.c_int)
CFUNCTYPE5 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                             ctypes
