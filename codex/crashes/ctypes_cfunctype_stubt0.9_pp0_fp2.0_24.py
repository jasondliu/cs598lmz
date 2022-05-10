import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.pythonapi.Py_GetPythonDLL()
assert fun() != None, "Py_GetPythonDLL() returned None"
