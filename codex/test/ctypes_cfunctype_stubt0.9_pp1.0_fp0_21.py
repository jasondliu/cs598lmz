import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

s = ctypes.pythonapi.PyTuple_New.argtypes

