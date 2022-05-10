import ctypes
# Test ctypes.CFUNCTYPE
PYFUNC =  ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)
ctypes.cast( PYFUNC( pow ), ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_double, ctypes.c_double ) )

