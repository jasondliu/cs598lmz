import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

import ctypes
import ctypes.util
lib = ctypes.util.find_library('m')
