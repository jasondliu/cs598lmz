import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def func(a,b,c):
	print(a,b,c,c[0],c[1])
	return 1

lib = ctypes.CDLL("./libtest.so")
lib.set_callback.argtypes = [FUNTYPE]
lib.set_callback(FUNTYPE(func))
lib.call1(1,2)
lib.call2(1,2)
