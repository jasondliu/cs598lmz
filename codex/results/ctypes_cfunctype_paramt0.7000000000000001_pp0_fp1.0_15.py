import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)
fun = FUNTYPE(myadd)
res = fun(1,2)
print(res)
