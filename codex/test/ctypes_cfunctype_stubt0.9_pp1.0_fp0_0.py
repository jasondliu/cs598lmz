import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

type(fun)

# fun.__class__
instancemethod = type(fun)
instancemethod

#fun.__class__ = object
type(fun)

