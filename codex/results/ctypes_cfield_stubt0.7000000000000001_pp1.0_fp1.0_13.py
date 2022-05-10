import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def cfield_fromaddress(addr, ctype):
    if not isinstance(ctype, ctypes.CField):
        raise TypeError(ctype)
    obj = object.__new__(ctype)
    obj.__dict__['_b_base_'] = addr
    return obj

def cfield_fromvalue(value, ctype):
    if not isinstance(ctype, ctypes.CField):
        raise TypeError(ctype)
    obj = object.__new__(ctype)
    obj.__dict__['_b_base_'] = ctypes.addressof(value)
    return obj

def cfield_cast(obj, ctype):
    if obj._b_base_ is None:
        raise TypeError(obj)
    ctype = ctypes._pointer_type_cache(ctype)
    return ctype.from_address(obj._b_base_)

def cfield_address(obj):
    if obj._b_base_ is None:
        raise TypeError(obj)
    return obj._b
