import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 42
fun()['x'] = 4
print fun() is fun()
