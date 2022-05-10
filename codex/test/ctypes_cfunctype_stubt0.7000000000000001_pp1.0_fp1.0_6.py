import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return

import _ctypes
_ctypes.PyObj_FromPtr(ctypes.cast(fun, ctypes.c_void_p).value)
