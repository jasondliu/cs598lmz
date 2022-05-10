import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "xyz"

PyCode_New = ctypes.pythonapi.PyCode_New
PyCode_New.restype = ctypes.py_object
