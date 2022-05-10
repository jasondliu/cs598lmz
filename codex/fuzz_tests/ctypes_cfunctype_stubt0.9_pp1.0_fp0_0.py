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

instancemethod.__dict__['__call__'].__get__(fun)

instancemethod.__dict__['__call__'].__get__(fun).__name__

instancemethod.__dict__['__get__'].__get__(instancemethod.__dict__['__call__']).__name__

instancemethod.__dict__['__call__'].__get__(fun).__qualname__
instancemethod.__dict__['__get__'].__get__(instancemethod.__dict__['__call__']).__qualname__

instancemethod.__dict__['__get__'].__get__(instancemethod.__dict__['__get__'])
instancemethod.__dict__['__get__'].__get__(instancemethod.__dict__['__hash__'])

#instancemethod.__dict__['__get__'].__get__
