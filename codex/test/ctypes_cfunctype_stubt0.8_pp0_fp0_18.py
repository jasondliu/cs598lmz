import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def class_(val):
    if isinstance(val, ctypes.py_object):
        return type(val)

def new(typ, obj):
    if isinstance(typ, type) and isinstance(obj, typ):
        return obj

def instance(inst, typ):
    if isinstance(inst, typ):
        return True
    return False

def builtin(inst):
    return inst

def subtype(sub, sup):
    return issubclass(sub, sup)

def getattr(typ, attr):
    return getattr(typ, attr)

def setattr(typ, attr, val):
    setattr(typ, attr, val)

def delattr(typ, attr):
    delattr(typ, attr)

def call(typ, args, kwargs):
    return typ(*args, **kwargs)

