import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b'abc'

ctypes.pythonapi.PyObject_SetAttr.argtypes = (ctypes.py_object, ctypes.py_object, ctypes.py_object)

