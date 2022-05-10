import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)
build_fun = lambda x: lambda n: n*x

funs = [build_fun(i) for i in range(20)]
C_FUNS = [FUNTYPE(s) for s in funs]
