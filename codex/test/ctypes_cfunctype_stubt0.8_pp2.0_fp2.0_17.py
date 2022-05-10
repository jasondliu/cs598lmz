import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

'''Error already raised in ffi:e: error: '+' not supported between instances of
'_ctypes.PyCFuncPtrType' and 'str'''

