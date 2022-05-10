import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float)

import numpy as np
from numpy.ctypeslib import ndpointer

_lib.getShape.argtypes = [FUNTYPE, ndpointer(np.int32)] # input argument types
_lib.getShape.restype = ndpointer(np.int32) # return type


# __file__ for windows
_lib.getWeight.argtypes = [ctypes.c_char_p, FUNTYPE, ndpointer(np.int32)] # input argument types
_lib.getWeight.restype = ndpointer(np.float32) # return type

def getWeight(filename, fun, shape):
	filename = bytes(filename, encoding='utf-8')
	p_d = np.zeros(shape, np.float32)
	shape = np.array(shape, np.int32)
	nr,nc = shape[:2]

	cfun = FUNTYPE(fun)
	p_w = _lib.getWeight(filename, cfun, shape)

	for k in range(shape[2]):
	
