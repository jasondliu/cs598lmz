import ctypes
# Test ctypes.CFUNCTYPE
import _testcapi

def PyCFuncPtr_Check(obj):
    if not isinstance(obj, ctypes.CFUNCTYPE):
        return 0
    return 1

def PyCFuncPtr_CheckExact(obj):
    if not type(obj) is ctypes.CFUNCTYPE:
        return 0
    return 1

def PyCFuncPtr_GetFuncDescr(obj):
    if not isinstance(obj, ctypes.CFUNCTYPE):
        raise TypeError, "must be a ctypes callback type"
    return obj._flags_

def PyCFuncPtr_GetFunc(obj):
    if not isinstance(obj, ctypes.CFUNCTYPE):
        raise TypeError, "must be a ctypes callback type"
    return ctypes.cast(ctypes.addressof(obj), ctypes.c_void_p).value

def PyCFuncPtr_Call(obj, args, kwds):
    if not isinstance(obj, ctypes.CFUNCTYPE) or type(obj)
