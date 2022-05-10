import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():  
    return [42]

ctypes.pythonapi.PyList_GetItem.restype = ctypes.py_object

ctypes.pythonapi.PyList_GetItem(fun(), 0)
</code>

