import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return True
#fun
#AttributeError: 'NoneType' object has no attribute '__call__'
