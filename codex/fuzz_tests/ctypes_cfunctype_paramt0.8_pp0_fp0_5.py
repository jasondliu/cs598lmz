import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
)

#
# C VARIABLES
#
CSIZE = ctypes.c_int.in_dll(_libs['aem2d'], 'CSIZE').value
NSIZE = ctypes.c_int.in_dll(_libs['aem2d'], 'NSIZE').value
RSIZE = ctypes.c_int.in_dll(_libs['aem2d'], 'RSIZE').value
ECSIZE = ctypes.c_int.in_dll(_libs['aem2d'], 'ECSIZE').value

#
# FUNCTIONS
#
# int fh2d_(const int *, const float *, const float
