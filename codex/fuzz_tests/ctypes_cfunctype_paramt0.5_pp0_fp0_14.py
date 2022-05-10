import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
	print(x, y)
	return x + y

cb = FUNTYPE(callback)

lib.test_callback(ctypes.c_int(1), ctypes.c_int(2), cb)
