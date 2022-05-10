import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
mylib.myfunction.restype = FUNTYPE
mylib.myfunction.argtypes = None
