import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# class PyObject(ctypes.c_void_p):
#     pass

# PyObject_GetAttrString = ctypes.pythonapi.PyObject_GetAttrString
# PyObject_GetAttrString.argtypes = [PyObject, ctypes.c_char_p]
# PyObject_GetAttrString.restype = PyObject

# PyCallable_Check = ctypes.pythonapi.PyCallable_Check
# PyCallable_Check.argtypes = [PyObject]
# PyCallable_Check.restype = ctypes.c_int

# PyObject_CallFunction = ctypes.pythonapi.PyObject_CallFunction
# PyObject_CallFunction.argtypes = [PyObject, ctypes.c_char_p, ctypes.c_void_p]
# PyObject_CallFunction.restype = PyObject

# PyObject_CallFunctionObjArgs = ctypes.pythonapi.PyObject_CallFunctionObjArgs
# PyObject_CallFunctionObjArgs.argtypes = [PyObject, ..., ctypes
