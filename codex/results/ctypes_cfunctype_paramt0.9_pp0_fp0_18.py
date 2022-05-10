import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint), ctypes.c_double, ctypes.POINTER(ctypes.c_double),  ctypes.c_void_p, ctypes.c_double, ctypes.POINTER(ctypes.c_uint))
