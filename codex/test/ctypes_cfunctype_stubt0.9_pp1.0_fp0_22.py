import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): 
    ... 
ctypes.cast(fun, ctypes.py_object)
