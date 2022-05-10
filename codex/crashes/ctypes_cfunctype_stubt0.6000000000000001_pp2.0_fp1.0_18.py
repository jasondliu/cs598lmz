import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123
ctypes.pythonapi.PyObject_SetAttrString(ctypes.py_object(fun),
                                        "__call__",
                                        fun)
