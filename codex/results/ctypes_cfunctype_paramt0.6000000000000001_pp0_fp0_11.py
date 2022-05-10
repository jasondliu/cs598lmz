import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def my_callback(a,b):
	return a+b

f = FUNTYPE(my_callback)

print (f(1,2))
