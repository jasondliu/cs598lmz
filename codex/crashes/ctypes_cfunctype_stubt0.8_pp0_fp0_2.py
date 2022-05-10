import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
try:
    ctypes.pythonapi.PyType_Ready(fun)
except:
    pass
