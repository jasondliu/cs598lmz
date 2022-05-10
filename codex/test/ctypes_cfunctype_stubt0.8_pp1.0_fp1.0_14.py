import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

import _ctypes
_ctypes.PyObj_FromPtr(ctypes.addressof(fun))
