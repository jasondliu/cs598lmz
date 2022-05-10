import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = FUNTYPE(lambda x,y: x+y)
print(f(1,2))

f = FUNTYPE(lambda x,y: x*y, use_errno=True, use_last_error=True)
print(f(4,5))
