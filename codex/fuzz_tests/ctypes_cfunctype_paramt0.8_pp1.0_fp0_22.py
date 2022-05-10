import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f = FUNTYPE(lambda n: n*2)
ret = f(2)
print(ret)
