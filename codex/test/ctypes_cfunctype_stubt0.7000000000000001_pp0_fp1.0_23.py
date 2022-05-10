import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# This is a C-level cast, so it doesn't use the python level __int__ method
