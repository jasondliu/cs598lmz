import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
s = ctypes.pythonapi.PyObject_Str
s(fun)
