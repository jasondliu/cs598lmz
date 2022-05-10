import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    ctypes.pythonapi.PyErr_SetObject(ctypes.py_object(SystemError), ctypes.py_object(SystemError("error")))
    return None
