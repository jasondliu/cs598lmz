import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.pythonapi.PyFloat_AsDouble.restype(ctypes.py_object)
