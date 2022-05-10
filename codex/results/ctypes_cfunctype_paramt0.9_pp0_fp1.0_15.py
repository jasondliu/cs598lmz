import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
FUN = FUNTYPE(FF)

print(FUN(2.0, 3))
print(FF(2.0, 3))
FF.restype = ctypes.c_longdouble
FF.argtypes = (ctypes.c_longdouble, ctypes.c_longdouble)
print(FF(2.0, 3))
