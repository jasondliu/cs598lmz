import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
ctypes.pythonapi.PyObject_CallFunction(fun, None)
