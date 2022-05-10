import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 'hello'

print fun()

print fun.__name__

print fun.__module__
