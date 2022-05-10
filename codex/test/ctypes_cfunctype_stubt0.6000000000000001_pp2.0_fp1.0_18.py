import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123

fun()

ctypes.pythonapi.PyObject_SetAttrString(ctypes.py_object(fun),
                                        "__call__",
                                        fun)

fun()
