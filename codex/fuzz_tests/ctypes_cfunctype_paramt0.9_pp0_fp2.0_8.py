import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int)
cfun_struct = FUNTYPE(cfun)
print(cfun_struct(2, 10))
