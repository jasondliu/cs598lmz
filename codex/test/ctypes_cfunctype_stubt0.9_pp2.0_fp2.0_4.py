import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 'hi'

s = ctypes.string_at(FUNTYPE(fun)())
