import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
def callback(context, value):
	print("called from c with: %d, %d" % (context, value))
CALL_C_FROM_PY = CALLBACK_TYPE(callback)
		
def set_callback(callback):
	CALL_C_FROM_PY = CALLBACK_TYPE(callback)
	
library = ctypes.CDLL("./extension.dll")

# this is a C function that takes a python function as an argument
library.set_callback(CALL_C_FROM_PY);

# these are C functions that are bound to python
library.c_function.argtypes = [FUNTYPE]
library.call_in_python.argtypes = [FUNTYPE, ctypes.c_int]
library.call_in_python.restype = ctypes.c_int
library.
