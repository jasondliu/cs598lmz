import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
print(fun())

import ctypes
import os
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# Cast the Python function to a C function
f = FUNTYPE(os.system)
